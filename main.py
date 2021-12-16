# -*- coding: utf-8 -*-

#
# Super minimalistic example of performing a Swish payment
#
# Dependencies: flask , requests
#
#
import json
import requests
from urllib.parse import urljoin
from flask import Flask, request, make_response


# 1
# setup Flask applicationm
app = Flask(__name__)
app.debug = True



# 2
# add a route to handle Swish callbacks
#
# This would normally be your
@app.route("/swish/callback", methods=["POST"])
def swish_callback():

    print("******************")
    print("Swish Callback ***")
    print(json.dumps(request.json, indent=2))

    return make_response("This is fine", 200)



# 3
# initiate a Swish payement
#
# You need a NGROK callback tunnel setup. See https://ngrok.com
#
NGROK_URL = "https://08c3-178-132-253-148.ngrok.io"

SWISH_CALLBACKURL = urljoin(NGROK_URL, "/swish/callback")

SWISH_PAYEEALIAS = "1231181189" # This would be your merchant swish number in production. In test it doesnt matter

SWISH_ROOTCA = "./CERTIFICATES/Swish_TLS_RootCA.pem"
SWISH_CERT = ("./CERTIFICATES/Swish_Merchant_TestCertificate_1234679304.pem", "./CERTIFICATES/Swish_Merchant_TestCertificate_1234679304-nopw.key")

SWISH_URL = "https://mss.cpc.getswish.net/swish-cpcapi/api/"
#SWISH_URL = "https://cpc.getswish.net/swish-cpcapi/api/" # PRODUCTION


payload = {
    "payeePaymentReference": "0123456789",
    "callbackUrl": SWISH_CALLBACKURL,
    "payeeAlias": SWISH_PAYEEALIAS,
    "payerAlias": "46701234567",    # Payers (your) phone number
    "currency": "SEK",
    "amount": "2",
    "message": "100-pack plastpåsar"
}

resp = requests.post(urljoin(SWISH_URL, "v1/paymentrequests"), json=payload, cert=SWISH_CERT, verify=SWISH_ROOTCA, timeout=2)
print(resp.status_code, resp.content)



# 4
# start the webserver to process incoming requests (Swish callback)
from werkzeug.serving import run_simple

run_simple('0.0.0.0', 8001,app, use_debugger=True, use_reloader=True)
