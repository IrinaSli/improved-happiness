import requests
from endpoints.endpoint import Endpoint


class GetMeme(Endpoint):
    def get_memes(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url = f"{self.url}/meme",
            headers=headers
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        return

    def get_one_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f"{self.url}/meme/{meme_id}",
            headers=headers
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = None
        return
