from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "owner": "@mynk_mynk_mynk",
        "message": "LPG Info API"
    })

@app.route('/lpg-info', methods=['GET', 'POST'])
def get_lpg_info():

    # GET / POST support
    if request.method == 'GET':
        mobile_no = request.args.get('mobile_no')
    else:
        data = request.get_json()
        mobile_no = data.get('mobile_no') if data else None

    # Check mobile number
    if not mobile_no:
        return jsonify({
            "success": False,
            "message": "Mobile number is required"
        }), 400

    # API URL
    url = "https://apigw.umangapp.in/ioclApi/ws1/consumervalidate"

    # Headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/json',
        'subsid': '0',
        'sec-ch-ua-platform': '"Android"',
        'deptid': '186',
        'tenantid': '',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'formtrkr': '0',
        'x-api-key': 'VKE9PnbY5k1ZYapR5PyYQ33I26sXTX569Ed7eqyg',
        'sec-ch-ua-mobile': '?1',
        'srvid': '1123',
        'subsid2': '0',
        'origin': 'https://web.umang.gov.in',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://web.umang.gov.in/',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=1, i'
    }

    # Cookies
    cookies = {
        'AWSALB': 'test',
        'AWSALBCORS': 'test'
    }

    # Payload
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
            cookies=cookies,
            json=payload,
            timeout=30
        )

        try:
            result = response.json()
        except:
            return jsonify({
                "success": False,
                "message": "Invalid JSON response",
                "raw": response.text
            }), 500

        return jsonify({
            "success": True,
            "owner": "@mynk_mynk_mynk",
            "response": result
        }), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


# Vercel Handler
app = app
