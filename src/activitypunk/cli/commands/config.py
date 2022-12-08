

from activitypunk.cli.commands.command import Command
from activitypunk.config import ActivityPunkConfig


class ConfigCommand(Command):

    name = "config"
    description = "Get ActivityPunk configuration"

    def __init__(self, *args):

        super().__init__(*args)

    @staticmethod
    def main(args):

        print(args.config.user_at_host)
        

