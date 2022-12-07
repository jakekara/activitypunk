from activitypunk_jakekara.cli.commands.command import Command
from activitypunk_jakekara.user import User
from activitypunk_jakekara.webfinger import Webfinger
import json


class WebfingerCommand(Command):

    name = "webfinger"
    description = "Get webfinger JSON for a given user (user@host)"

    def __init__(self, *args):

        super().__init__(*args)
        self.parser.add_argument("user")

    @staticmethod
    def main(args):
        
        print(f"webfinger {args.user}")

        user = User.from_user_at_host(args.user)

        webfinger = Webfinger(user)
        
        print(json.dumps(webfinger.data, indent=2))
        