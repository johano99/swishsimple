import requests
import json
from urllib.parse import urljoin
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint 

def index(request):
 
    NGROK_URL = "https://e40c-92-33-202-136.ngrok.io/"

    SWISH_CALLBACKURL = urljoin(NGROK_URL, "/swish/callback")

    SWISH_PAYEEALIAS = "1231231231" # This would be your merchant swish number in production. In test it doesnt matter

    SWISH_ROOTCA = "/code/Certificates/Swish_TLS_RootCA.pem"
    SWISH_CERT = ("/code/Certificates/Swish_Merchant_TestCertificate_1234679304.pem", "/code/Certificates/Swish_Merchant_TestCertificate_1234679304-nopw.key")

    SWISH_URL = "https://mss.cpc.getswish.net/swish-cpcapi/api/"
    #SWISH_URL = "https://cpc.getswish.net/swish-cpcapi/api/" # PRODUCTION


    payload = {
        "payeePaymentReference": "0123456789",
        "callbackUrl": SWISH_CALLBACKURL,
        "payeeAlias": SWISH_PAYEEALIAS,
        "payerAlias": "4672193819",    # Payers (your) phone number
        "currency": "SEK",
        "amount": "2",
        "message": "100-pack plastpåsar"
    }

    resp = requests.post(urljoin(SWISH_URL, "v1/paymentrequests"), json=payload, cert=SWISH_CERT, verify=SWISH_ROOTCA, timeout=2)
    print(resp.status_code, resp.text)

    return JsonResponse("Invoked swish-view", status=200, safe=False)

@csrf_exempt
def swish_callback(request):

    print("******************")
    print("Swish Callback ***")

    data=request.body
    data_dict = json.loads(data.decode("utf-8"))
    pprint(data_dict)

    return JsonResponse("This is fine", status=200, safe=False)