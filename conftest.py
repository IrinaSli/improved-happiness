import pytest
from endpoints.authorization import Authorization
from endpoints.delete_meme import DeleteMeme
from endpoints.endpoint import Endpoint
from endpoints.get_meme import GetMeme
from endpoints.post_meme import PostMeme
from endpoints.put_meme import PutMeme


@pytest.fixture(scope="session")
def auth_user():
    token = Authorization().get_token(name="Irina Test")
    Endpoint.headers["Authorization"] = f"{token}"

@pytest.fixture()
def get_all_memes_endpoint():
    return GetMeme()

@pytest.fixture()
def post_meme_endpoint():
    return PostMeme()

@pytest.fixture()
def put_meme_endpoint():
    return PutMeme()

@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()

@pytest.fixture()
def create_test_meme(post_meme_endpoint, delete_meme_endpoint):
    payload = {"text": "new meme 5",
               "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
               "tags": ["spider", "baby"],
               "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    meme_id = post_meme_endpoint.json['id']
    yield meme_id
    delete_meme_endpoint.delete_meme(meme_id)
