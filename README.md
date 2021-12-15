# Flask/Django application for managing payments with Swedish bank-collaboration application Swish

This little example application give you the set-up for how to integrating Swish payments on your website with Flask or Django. 

The certificates you find in the project are the test-certificates that are supplied by Swish for trying out your application before setting it up to do real payments. Note that these test certificates get renewed from time to time, so when you are trying this out, you may have to download the new ones, you can find the link to the certificates on the swish developer site.

Also, you will need to convert the following certificate to not use a password (they are originally password protected, which create problem when trying to prompt the web-application for the passsword):

Swish_Merchant_TestCertificate_1234679304.key

The password for this certificate has been removed and can be found in the "CERTIFICATES" folder, where it ends with "nopw.key". You can find out how to remove the password for a certificate here:

https://help.cloud66.com/maestro/how-to-guides/security/remove-passphrase.html


For more information about how to set up Swish on your website please go to the official site for developers:

https://developer.swish.nu/

Here you will also find how to your company to retrieve your own Swish certificates so you can start offering your customers to do payment to your own Swish-number. 

## Instructions

* Download repo
* Create Ngrok account 
* Set up Ngrok to tunnel your localhost
* Run application


## For use in Django

To use this set-up with Django, create two views, one for invoking the payment call, one acting as a call-back (where you will check if the payment went trough or not). Make sure to set up urls to the views (also given in example) and install the requirements.





