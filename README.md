# A minimalistic Flask/Django application demonstrating how to manage payments with Swedish bank-collaboration application Swish

## Setting up a test environment

This little example application give you the set-up for how to integrating Swish payments on your website with Flask or Django. 

The certificates you find in the project are the test-certificates that are supplied by Swish for trying out your application before setting it up to do real payments. Note that these test certificates get renewed from time to time, so when you are trying this out, you may have to download the new ones, you can find the link to the certificates on the swish developer site.

Also, you will need to convert the following certificate to not use a password (they are originally password protected, which create problem when trying to prompt the web-application for the passsword):

Swish_Merchant_TestCertificate_1234679304.key

The password for this certificate has been removed and can be found in the "CERTIFICATES" folder, where it ends with "nopw.key". You can find out how to remove the password for a certificate here:

https://help.cloud66.com/maestro/how-to-guides/security/remove-passphrase.html


For more information about how to set up Swish on your website please go to the official site for developers:

https://developer.swish.nu/

Here you will also find how to your company to retrieve your own Swish certificates so you can start offering your customers to do payment to your own Swish-number. 

### Instructions

* Download repo
* Create Ngrok account 
* Set up Ngrok to tunnel your localhost
* Run application

## Setting up a production environment

* Register with your bank to get a Swish Handel agreement
* Log into the Swish Certificate Portal: https://portal.swish.nu/company/certificates/ 
* Follow the steps to generate a certificate (when you generate your key, you don't have to fill out a password) and save it to a folder. This file will have the name of something like: swish_certificate_202112155823.pem - this is your certificate file.
* Now head into your keychain access on your mac, go under the "keys" tab and locate the key that has been created for you (4 096-bit), right click on it and press export. This will have the name of something like yourusername.p12 - this is your private key.
* You will need to convert your private key from .p12 format to .key format. See how to do that here: https://stackoverflow.com/questions/16075846/how-to-change-a-p12-file-to-key-file?fbclid=IwAR02Ao0BVSHU2raoRHarjjRkkyAHUjYuoUWKGT10XQRn4m9PrEdvzlSGubM 
* You will now have 2 files - your certificate file and your private.key file. Copy these files to your CERTIFICATES folder along with the Swish_TLS_RootCA.pem file which you got when you downloaded the test-certificate files. This file is used to verify that you are working toward the correct host.
* Change to using the production endpoint by commenting out the SWISH_URL for testing purposes and activating the production SWISH_URL.
* Make sure that you have filled out the SWISH_PAYEEALIAS with the Swish-number for your company and the payerAlias in the payload with your number (for testing generating a payment at your phone)
* Run the application again as you did in the test environment and check your swish application in your phone and you should have recieved a payment request!



## For use in Django

To use this set-up with Django, create two views, one for invoking the payment call, one acting as a call-back (where you will check if the payment went trough or not). Make sure to set up urls to the views (also given in example) and install the requirements.





