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

#positive tests - status 200
def test_get_all_memes(auth_user, get_all_memes_endpoint):
    get_all_memes_endpoint.get_memes()
    get_all_memes_endpoint.check_status_is_200()

def test_get_one_meme(post_meme_endpoint, get_all_memes_endpoint):
    payload = {"text": "new meme 5",
               "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
               "tags": ["spider", "baby"],
               "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    meme_id = post_meme_endpoint.json["id"]
    get_all_memes_endpoint.get_one_meme(meme_id)
    get_all_memes_endpoint.check_status_is_200()

@pytest.mark.parametrize('test_data', new_memes)
def test_post_new_meme(post_meme_endpoint, delete_meme_endpoint, test_data):
    post_meme_endpoint.post_meme(payload=test_data)
    post_meme_endpoint.check_response_text_is_correct(test_data["text"])
    post_meme_endpoint.check_response_tags_correct(test_data["tags"])
    post_meme_endpoint.check_status_is_200()
    meme_id = post_meme_endpoint.json["id"]
    delete_meme_endpoint.delete_meme(meme_id)

def test_put_meme(post_meme_endpoint, put_meme_endpoint, delete_meme_endpoint):
    payload = {"text": "new meme 5",
               "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
               "tags": ["spider", "baby"],
               "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    meme_id = post_meme_endpoint.json["id"]
    new_payload = {"id": meme_id,
                   "text": "edited name",
                   "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
                   "tags": ["spider", "cry"],
                   "info": {"objects": ["girl", "house"]}}
    put_meme_endpoint.put_meme(meme_id, new_payload)
    put_meme_endpoint.check_status_is_200()
    put_meme_endpoint.check_response_text_is_correct(new_payload["text"])
    delete_meme_endpoint.delete_meme(meme_id)

def test_delete_meme(post_meme_endpoint, delete_meme_endpoint):
    payload =  {"text": "new meme 5",
    "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
    "tags": ["spider", "baby"],
    "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    meme_id = post_meme_endpoint.json["id"]
    delete_meme_endpoint.delete_meme(meme_id)
    delete_meme_endpoint.check_status_is_200()
    delete_meme_endpoint.check_that_delete_is_successful(meme_id)

#negative tests
def test_get_meme_with_wrong_id(get_all_memes_endpoint):
    get_all_memes_endpoint.get_one_meme(meme_id="test")
    get_all_memes_endpoint.check_status_is_404()

def test_text_is_required(post_meme_endpoint):
    payload = {"url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
               "tags": ["spider", "baby"],
               "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    post_meme_endpoint.check_status_is_400()

def test_url_is_required(post_meme_endpoint):
    payload = {"text": "New name",
               "tags": ["spider", "baby"],
               "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    post_meme_endpoint.check_status_is_400()

def test_tags_is_required(post_meme_endpoint):
    payload = {"text": "New name",
               "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
               "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    post_meme_endpoint.check_status_is_400()

def test_info_is_required(post_meme_endpoint):
    payload = {"text": "New name",
               "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
               "tags": ["spider", "baby"]}
    post_meme_endpoint.post_meme(payload)
    post_meme_endpoint.check_status_is_400()

def test_put_meme_id_is_required(post_meme_endpoint, put_meme_endpoint, delete_meme_endpoint):
    payload = {"text": "new meme 5",
               "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
               "tags": ["spider", "baby"],
               "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    meme_id = post_meme_endpoint.json["id"]
    new_payload = {"text": "edited name",
                   "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
                   "tags": ["spider", "cry"],
                   "info": {"objects": ["girl", "house"]}}
    put_meme_endpoint.put_meme(meme_id, new_payload)
    put_meme_endpoint.check_status_is_400()

def test_put_meme_text_is_required(post_meme_endpoint, put_meme_endpoint, delete_meme_endpoint):
    payload = {"text": "new meme 5",
               "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
               "tags": ["spider", "baby"],
               "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    meme_id = post_meme_endpoint.json["id"]
    new_payload = {"id": meme_id,
                   "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
                   "tags": ["spider", "cry"],
                   "info": {"objects": ["girl", "house"]}}
    put_meme_endpoint.put_meme(meme_id, new_payload)
    put_meme_endpoint.check_status_is_400()
    delete_meme_endpoint.delete_meme(meme_id)

def test_put_meme_url_is_required(post_meme_endpoint, put_meme_endpoint, delete_meme_endpoint):
    payload = {"text": "new meme 5",
               "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
               "tags": ["spider", "baby"],
               "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    meme_id = post_meme_endpoint.json["id"]
    new_payload = {"id": meme_id,
                   "text": "edited name",
                   "tags": ["spider", "cry"],
                   "info": {"objects": ["girl", "house"]}}
    put_meme_endpoint.put_meme(meme_id, new_payload)
    put_meme_endpoint.check_status_is_400()
    delete_meme_endpoint.delete_meme(meme_id)

def test_put_meme_tags_is_required(post_meme_endpoint, put_meme_endpoint, delete_meme_endpoint):
    payload = {"text": "new meme 5",
               "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
               "tags": ["spider", "baby"],
               "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    meme_id = post_meme_endpoint.json["id"]
    new_payload = {"id": meme_id,
                   "text": "edited name",
                   "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
                   "info": {"objects": ["girl", "house"]}}
    put_meme_endpoint.put_meme(meme_id, new_payload)
    put_meme_endpoint.check_status_is_400()
    delete_meme_endpoint.delete_meme(meme_id)

def test_put_meme_info_is_required(post_meme_endpoint, put_meme_endpoint, delete_meme_endpoint):
    payload = {"text": "new meme 5",
               "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
               "tags": ["spider", "baby"],
               "info": {"objects": ["girl", "house"]}}
    post_meme_endpoint.post_meme(payload)
    meme_id = post_meme_endpoint.json["id"]
    new_payload = {"id": meme_id,
                   "text": "edited name",
                   "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bbc.com%2Fbbcthree%2Farticle%2Fe6511d6a-ea8c-4e27-aac3-728205903635&psig=AOvVaw19wMSziOILgg7_94nOrjtk&ust=1748937073618000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIjKxbug0o0DFQAAAAAdAAAAABAE",
                   "tags": ["spider", "cry"]}
    put_meme_endpoint.put_meme(meme_id, new_payload)
    put_meme_endpoint.check_status_is_400()
    delete_meme_endpoint.delete_meme(meme_id)

def test_delete_meme_incorrect_id(post_meme_endpoint, delete_meme_endpoint):
    delete_meme_endpoint.delete_meme(0)
    delete_meme_endpoint.check_status_is_404()
