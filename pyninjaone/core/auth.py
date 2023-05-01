import requests
import json

class NinjaOneAuthenitcator():

    def __init__(self, client_id, client_secret_key, scope, grant_type, redirect_url, code=None):
        self.client_id = client_id
        self.client_secret_key = client_secret_key
        self.scope = scope
        self.grant_type = grant_type
        self.redirect_url = redirect_url
        self.code = code

    def generate_token(self):
        url = "https://app.ninjarmm.com/ws/oauth/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json"
        }

        data = {
            "grant_type": self.grant_type,
            "client_id": self.client_id,
            "client_secret": self.client_secret_key,
            "scope": self.scope,
            "code": self.code,
            "redirect_url": self.redirect_url

        }

        response = requests.post(url=url, headers=headers, data=data)
        if response.status_code == 200:
            access_token = json.loads(response.text)["access_token"]
            return access_token
        else:
            raise Exception("Error:", response.text)
