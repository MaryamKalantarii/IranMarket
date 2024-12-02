import requests
import json
from django.conf import settings

class ZarinPalSandbox:
    _payment_request_url = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"
    _payment_verify_url = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"
    _payment_page_url = "https://sandbox.zarinpal.com/pg/StartPay/"
    _callback_url = "https://sandbox.zarinpal.com/pg/StartPay/"

    def __init__(self, merchant_id=settings.MERCHANT_ID):
        if not merchant_id:
            raise ValueError("Merchant ID is not set")
        self.merchant_id = merchant_id

    def payment_request(self, amount, description="پرداختی کاربر"):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        
        payload = {
            "merchant_id": self.merchant_id,
            "amount": str(amount),
            "callback_url": self._callback_url,
            "description": description,
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(
            self._payment_request_url, headers=headers, data=json.dumps(payload))

        return response.json()

        # try:
        #     response = requests.post(
        #         self._payment_request_url, headers=headers, data=json.dumps(payload))
        #     response.raise_for_status()
        #     response_data = response.json()

        #     if response_data.get("Status") != 100:
        #         raise ValueError(f"Payment request failed: {response_data.get('Status')}")
        #     return response_data
        # except Exception as e:
        #     print(f"Error in payment_request: {e}")
        #     raise

    def payment_verify(self, amount, authority):
        if not authority:
            raise ValueError("Authority is required for verification")
        
        payload = {
            "merchant_id": self.merchant_id,
            "amount": amount,
            "authority": authority
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(
            self._payment_verify_url, headers=headers, data=json.dumps(payload))
        return response.json()

        # try:
        #     response = requests.post(
        #         self._payment_verify_url, headers=headers, data=json.dumps(payload))
        #     response.raise_for_status()
        #     response_data = response.json()

        #     if response_data.get("Status") != 100:
        #         raise ValueError(f"Payment verification failed: {response_data.get('Status')}")
        #     return response_data
        # except Exception as e:
        #     print(f"Error in payment_verify: {e}")
        #     raise

    def generate_payment_url(self, authority):
        if not authority:
            raise ValueError("Authority is missing")
        return f"{self._payment_page_url}{authority}"
