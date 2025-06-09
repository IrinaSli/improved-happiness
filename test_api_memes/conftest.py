import pytest

from test_api_memes.endpoints.authorization import Authorization
from test_api_memes.endpoints.delete_meme import DeleteMeme
from test_api_memes.endpoints.endpoint import Endpoint
from test_api_memes.endpoints.get_meme import GetMeme
from test_api_memes.endpoints.post_meme import PostMeme
from test_api_memes.endpoints.put_meme import PutMeme


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

