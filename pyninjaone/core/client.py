import requests
class NinjaOneClient():

    def __init__(self, access_token):
        self.access_token = access_token

    def make_request(self, url, headers=None, data=None, method="GET"):
        headers = headers or {}
        headers["Authorization"] = f"Bearer {self.access_token}"
        response = requests.request(method, url, headers=headers, data=data)
        return response