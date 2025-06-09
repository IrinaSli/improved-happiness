import requests
from test_api_memes.endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    def delete_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f"{self.url}/meme/{meme_id}",
            headers=headers
        )
        try:
            if self.response.text:
                self.json = self.response.json()
            else:
                self.json = None
        except ValueError:
            self.json = None
        return self.response
