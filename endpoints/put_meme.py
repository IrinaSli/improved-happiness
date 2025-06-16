import requests
from endpoints.endpoint import Endpoint


class PutMeme(Endpoint):
    def put_meme(self, meme_id, new_payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f"{self.url}/meme/{meme_id}",
            json = new_payload,
            headers = headers
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        return
