import requests
from endpoints.endpoint import Endpoint


class PostMeme(Endpoint):
    def post_meme(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f"{self.url}/meme",
            json = payload,
            headers = headers
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        return
