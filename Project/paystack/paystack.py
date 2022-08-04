from django.conf import settings
import requests

class PayStackPayment():
    SECRET_KEY = settings.PAYSTACK_PRIVATE_KEY
    base_url = 'https://api.paystack.co'

    def verify_payment(self, reference, *arg, **kwargs):
        path = f"/transaction/verify/{reference}"
        
        header = {
            "Authorization": f"Bearer {self.SECRET_KEY}",
            "Content_type": 'Application/json',
        }
        url =self.base_url + path
        response =  requests.get(url, headers=header)

        if response.status_code == 200:
            response_data = response.json()
            return response_data['status'], response_data['data']
        response_data = response.json()
        return response_data['status'], response_data['message']
