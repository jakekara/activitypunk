import json
from activitypunk_jakekara.actor import ActivityPubActor, ActivityPubFirstPartyActor
from activitypunk_jakekara.cli.commands.command import Command
from activitypunk_jakekara.user import User

class ActorCommand(Command):

    name = "actor"
    description = "Get actor JSON from a given user@host string"

    def __init__(self, *args):

        super().__init__(*args)

        self.parser.add_argument("user", type=str)
        self.parser.add_argument("--private-pem", type=str, required=False)

    @staticmethod
    def main(args):

        user = User.from_user_at_host(args.user)
        
        if args.private_pem:
            actor = ActivityPubFirstPartyActor(user)
            key_text = open(args.private_pem).read()
            try:
                actor.set_private_key(key_text)
            except:
                print(f"The private key provided does not match the public key at: {actor.webfinger.actor_url}")
                exit(1)            
        else:
             actor = ActivityPubActor(user)
            
        print(json.dumps(actor.data, indent=2))
