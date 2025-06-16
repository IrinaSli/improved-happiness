import requests
from endpoints.endpoint import Endpoint


class Authorization(Endpoint):
    def get_token(self, name: str):
        response = requests.post(
            url=f"{self.url}/authorize",
            json={"name": name},
            headers={"Content-Type": "application/json"}
        )
        token = response.json()["token"]
        return token
