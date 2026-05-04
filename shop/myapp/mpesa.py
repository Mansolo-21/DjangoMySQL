import requests
from requests.auth import HTTPBasicAuth
from decouple import config
import base64
from datetime import datetime

# Load credentials
CONSUMER_KEY = config('MPESA_CONSUMER_KEY')
CONSUMER_SECRET = config('MPESA_CONSUMER_SECRET')
SHORTCODE = config('MPESA_SHORTCODE')
PASSKEY = config('MPESA_PASSKEY')
ENV = config('MPESA_ENV', default='sandbox')

# API URLs
if ENV == 'sandbox':
    AUTH_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    STK_PUSH_URL = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
else:
    AUTH_URL = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    STK_PUSH_URL = 'https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest'


def get_access_token():
    response = requests.get(AUTH_URL, auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET))
    token = response.json().get('access_token')
    return token



def lipa_na_mpesa(phone_number, amount, account_reference='TestPayment', transaction_desc='Payment'):
    access_token = get_access_token()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password_str = SHORTCODE + PASSKEY + timestamp
    password = base64.b64encode(password_str.encode()).decode()

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    payload = {
        "BusinessShortCode": int(SHORTCODE),
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": int(amount),
        "PartyA": int(phone_number),
        "PartyB": int(SHORTCODE),
        "PhoneNumber": int(phone_number),
        "CallBackURL": "https://example.com/callback/",
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc
    }

    response = requests.post(STK_PUSH_URL, json=payload, headers=headers)
    print(response.json())  # <-- print the response for debugging
    return response.json()