import pytest


new_memes = [
    {"text": "new meme 5",
    "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
    "tags": ["spider", "baby"],
    "info": {"objects": ["girl", "house"]}},
    {"text": "new meme 6",
    "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fmailtrap.io%2Fblog%2Fqa-testing-memes%2F&psig=AOvVaw3O_3yzvkVvTlw2LTHQnth8&ust=1749036358877000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCLDe_a-S1Y0DFQAAAAAdAAAAABAE",
    "tags": ["house", "baby", "fire"],
    "info": {"objects": ["girl", "house"]}}
]

def test_get_memes_non_auth(get_all_memes_endpoint):
    get_all_memes_endpoint.get_memes()
    get_all_memes_endpoint.check_status_is_401()

@pytest.mark.parametrize('test_data', new_memes)
def test_post_new_meme_non_auth(post_meme_endpoint, delete_meme_endpoint, test_data):
    post_meme_endpoint.post_meme(payload=test_data)
    post_meme_endpoint.check_status_is_401()

def test_put_meme_non_auth(post_meme_endpoint, put_meme_endpoint, delete_meme_endpoint):
    new_payload = {"id": 1,
                   "text": "edited name",
                   "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
                   "tags": ["spider", "cry"],
                   "info": {"objects": ["girl", "house"]}}
    put_meme_endpoint.put_meme(1, new_payload)
    put_meme_endpoint.check_status_is_401()

def test_delete_meme_non_auth(post_meme_endpoint, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme(1)
    delete_meme_endpoint.check_status_is_401()
