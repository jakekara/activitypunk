from activitypunk_jakekara.user import User
import requests

class Webfinger:

    def __init__(self, user:User):
        self.user = user
        self.data = None
        self.actor_url = None

        self.load_webfinger_json()

    def load_webfinger_json(self):

        full_username = self.user.to_user_at_host()
        
        response = requests.get(
            f"https://{self.user.host}/.well-known/webfinger", 
            params={
                "resource": f"acct:{full_username}"
            })

        
        if response.status_code < 200 or response.status_code >= 300:
            raise Exception(f"Failed to load: {response.status_code}")

        self.data = response.json()

        links = self.data["links"]
        self.actor_url = list(
            filter(
                lambda x: x["rel"].lower() == "self", 
                links
            ))[0]["href"]
