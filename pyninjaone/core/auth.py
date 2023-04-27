from typing import Any
import requests

class NinjaOneAuthenitcator():

    def __init__(self, client_id, client_secret_key, scope, grant_type, redirect_url):
        self.client_id = client_id
        self.client_secret_key = client_secret_key
        self.scope = scope
        self.grant_type = grant_type
        self.redirect_url = redirect_url

    def generate_token(self):
        pass
