import base64
from activitypunk.config import ActivityPunkConfig
from activitypunk.user import User
from activitypunk.utils.parsers import UserStringTypes, determine_user_string_type
from activitypunk.webfinger import Webfinger
import requests
from OpenSSL import crypto


class ActivityPubKey:

    def __init__(self, *, id, public_key_pem):
        self.id = id
        self.public_key_pem = public_key_pem

    @staticmethod
    def from_dict(data):

        return ActivityPubKey(
            id=data["id"],
            public_key_pem=data["publicKeyPem"]
        )

class ActivityPubActor:

    def __init__(self, user:User):
        self.user = user
        self.webfinger = Webfinger(user)
        self.data = None
        self.public_key = None
        self.private_key = None
        self.inbox_url = None
        self.load_actor_json()

    @staticmethod
    def from_user_string(user_str):
        """
        Accept a user string in the form of user@host or an actor URI
        """

        str_type = determine_user_string_type(user_str)

        if str_type == UserStringTypes.USER_AT_HOST:
            return Webfinger.from_user_at_host_string(str)


    def load_actor_json(self):
        response = requests.get(self.webfinger.actor_url, headers={
            "Accept": 'application/ld+json; profile="https://www.w3.org/ns/activitystreams'
        })

        if response.status_code < 200 or response.status_code >= 300:
            raise Exception(f"Failed to load actor JSON ({response.status_code}): {response.content}")

        self.data = response.json()
        self.public_key = ActivityPubKey.from_dict(self.data["publicKey"])
        self.inbox_url = self.data["inbox"]
        self.shared_inbox_url = self.data.get("sharedInbox")

    def verify(self, *, signature:str,  plaintext):
        x509 = crypto.X509()
        public_key = crypto.load_publickey(crypto.FILETYPE_PEM, self.public_key.public_key_pem)
        x509.set_pubkey(public_key)
        crypto.verify(x509, signature=signature, data=plaintext, digest="sha256")

class ActivityPubFirstPartyActor(ActivityPubActor):

    """
    An ActivityPubActor for which you have the private key (e.g., you)
    """

    private_key = None

    def set_private_key(self, private_key):
        self.private_key = private_key
        self.test_private_key()

    def sign(self, plaintext, digest="sha256"):
        private_key = crypto.load_privatekey(crypto.FILETYPE_PEM, self.private_key)
        signed = crypto.sign(private_key, plaintext.encode(), digest=digest)
        return signed
    
    def test_private_key(self, message="hello world", verbose=False):
        """
        Make sure the private key corresponds to the public key fetched from
        the actor endpoint
        """
        signature = self.sign(message)
        self.verify(signature=signature, plaintext=message)

        if not verbose:
            return

        print(f"Signed message: '{message}'")
        print(f"Signature: {base64.b64encode( signature)}")



    @staticmethod
    def from_config(config:ActivityPunkConfig):
        user = User.from_user_at_host(config.user_at_host)
        ret = ActivityPubFirstPartyActor(user)
        ret.set_private_key(config.private_key)
        return ret