class Endpoint:
    url = "http://167.172.172.115:52355/"
    response = None
    json = None
    headers = {"Content-Type": "application/json"}

    def check_status_is_200(self):
        assert self.response.status_code == 200

    def check_status_is_401(self):
        assert self.response.status_code == 401

    def check_response_text_is_correct(self, text):
        assert self.json['text'] == text

    def check_response_tags_correct(self, tags):
        assert self.json['tags'] == tags

    def check_that_delete_is_successful(self, meme_id):
        assert self.response.text == f"Meme with id {meme_id} successfully deleted"

    #for negative
    def check_status_is_404(self):
        assert self.response.status_code == 404

    def check_status_is_400(self):
        assert self.response.status_code == 400
