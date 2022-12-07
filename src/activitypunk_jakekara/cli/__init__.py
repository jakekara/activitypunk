import argparse
from activitypunk_jakekara.cli.commands.actor import ActorCommand
from activitypunk_jakekara.cli.commands.config import ConfigCommand
from activitypunk_jakekara.cli.commands.inbox import InboxCommand
from activitypunk_jakekara.cli.commands.send_dm import SendDirectMessageCommand
from activitypunk_jakekara.cli.commands.webfinger import WebfingerCommand
from activitypunk_jakekara.config import ActivityPunkConfig

commands = [WebfingerCommand, ActorCommand, ConfigCommand, SendDirectMessageCommand, InboxCommand]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default=ActivityPunkConfig.DEFAULT_PROFILE_NAME)
    subparsers = parser.add_subparsers(help="commands", dest="command")


    for command in commands:
        command(subparsers)

    args = parser.parse_args()
    config = ActivityPunkConfig(profile_name=args.profile)


    for command in commands:
        if args.command == command.name:
            args.config = config
            command.main(args)
            break
