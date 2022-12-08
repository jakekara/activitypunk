
import json
from activitypunk.activities.direct_message import direct_message
from activitypunk.actor import ActivityPubActor, ActivityPubFirstPartyActor
from activitypunk.cli.commands.command import Command
from activitypunk.config import ActivityPunkConfig
from activitypunk.deliver import deliver
from activitypunk.user import User


class SendDirectMessageCommand(Command):

    name = "dm"
    description = "Send a direct message to a user"

    def __init__(self, *args):

        super().__init__(*args)

        self.parser.add_argument("--profile", default=ActivityPunkConfig.DEFAULT_PROFILE_NAME)
        self.parser.add_argument("--to", type=str, required=True)
        self.parser.add_argument("message", type=str)

    @staticmethod
    def main(args):

        config = ActivityPunkConfig(profile_name=args.profile)
        me = ActivityPubFirstPartyActor.from_config(config)

        recipient = ActivityPubActor(User.from_user_at_host(args.to))

        dm = direct_message(sender=me, recipient=recipient, message=args.message)

        response = deliver(
            document=json.dumps(dm),
            # I'm not sure why this only seems to work with Mastodon when
            # I use the shared inbox endpoint. If I send it directly to the
            # the inbox specified in the actor profile, I get a 
            # signature verification error.
            inbox_url=recipient.data["endpoints"]["sharedInbox"],
            host=recipient.user.host,
            actor=me
        )

        print(response.content)


