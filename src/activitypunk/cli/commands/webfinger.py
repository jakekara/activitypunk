from activitypunk.cli.commands.command import Command
from activitypunk.user import User
from activitypunk.webfinger import Webfinger
import json


class WebfingerCommand(Command):

    name = "webfinger"
    description = "Get webfinger JSON for a given user (user@host)"

    def __init__(self, *args):

        super().__init__(*args)
        self.parser.add_argument("user")

    @staticmethod
    def main(args):
        
        user = User.from_user_at_host(args.user)

        webfinger = Webfinger(user)
        
        print(json.dumps(webfinger.data, indent=2))
        