from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "message": "LPG Info API"
    })

@app.route('/lpg-info', methods=['GET', 'POST'])
def get_lpg_info():

    # GET or POST support
    if request.method == 'GET':
        mobile_no = request.args.get('mobile_no')
    else:
        data = request.get_json()
        mobile_no = data.get('mobile_no') if data else None

    if not mobile_no:
        return jsonify({
            "error": "Mobile number is required"
        }), 400

    url = 'https://apigw.umangapp.in/ioclApi/ws1/consumervalidate'

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x-api-key': 'VKE9PnbY5k1ZYapR5PyYQ33I26sXTX569Ed7eqyg',
        'origin': 'https://web.umang.gov.in',
        'referer': 'https://web.umang.gov.in/'
    }

    payload = {
        "tkn": "iad1cc7d81-1533-44b0-9967-35599386d3df/2",
        "trkr": "213132",
        "lang": "en",
        "lat": "21",
        "lon": "90",
        "lac": "90",
        "usag": "90",
        "apitrkr": "123234",
        "usrid": "09",
        "mode": "web",
        "pltfrm": "android",
        "did": "123234",
        "deptid": "186",
        "formtrkr": "0",
        "srvid": "1123",
        "subsid": "0",
        "subsid2": "0",
        "trackingId": "",
        "source": "UMANG",
        "mobile": mobile_no,
        "consumerId": "",
        "partnerCode": "",
        "consumerNumber": ""
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        try:
            return jsonify(response.json()), response.status_code
        except:
            return jsonify({
                "error": "Invalid response",
                "raw": response.text
            }), 500

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

# Vercel handler
app = app
