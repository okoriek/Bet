import json
from django.conf import settings
import requests

class FlutterWavePayment():
    SECRET_KEY = settings.FLUTTERWAVE_SECRET_KEY
    base_url = 'https://api.flutterwave.com/v3'

    def confirm_payment(self, reference, *arg, **kwargs):
        path = f"/transactions/?tx_ref={reference}"
        
        header = {
            "Authorization": f"Bearer {self.SECRET_KEY}",
            "Content_type": 'application/json',
        }
        url =self.base_url + path
        response =  requests.get(url, headers=header)

        if response.status_code == 200:
            response_data = response.json()
            return response_data['status'], response_data['data']
        response_data = response.json()
        return response_data['status'], response_data['message']

        
        
