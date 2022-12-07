import os
import shutil
from activitypunk_jakekara.cli.commands.command import Command
from activitypunk_jakekara.config import ActivityPunkConfig
from activitypunk_jakekara.inbox_manager.s3_activity import S3Activity
import subprocess

class InboxCommand(Command):

    name = "inbox"
    description = "inbox operations"

    def __init__(self, *args):

        super().__init__(*args)

        self.parser.add_argument("--sync-from-s3", action="store_true")

    def move_to_trash(config: ActivityPunkConfig, full_path):

        trash_dir = os.path.join(config.data_dir, "trash")
        if not os.path.exists(trash_dir):
            os.makedirs(trash_dir)

        dest = os.path.join(trash_dir, os.path.basename(full_path))

        shutil.move(full_path, dest)
        return dest


    def summarize(config: ActivityPunkConfig, args):
        inbox_dir = os.path.join(config.data_dir, "s3", "events")

        for file in os.listdir(inbox_dir):
            full_path = os.path.join(inbox_dir, file)
            try:
                activity = S3Activity(open(full_path).read())
            except:
                print("Invalid file. Moved to trash => ", InboxCommand.move_to_trash(config, full_path))
            print(f"{full_path}: {activity}")

    def sync_from_s3(config:ActivityPunkConfig):
        
        s3_bucket = config.s3_bucket
        if not s3_bucket:
            print("No s3 bucket")
            exit(1)
            
        data_dir = config.data_dir

        local_s3_dir = os.path.join(data_dir, "s3")

        print(f"Downloading from s3://{s3_bucket} to {local_s3_dir}")

        out = subprocess.run(" ".join(["aws", "s3", "sync", f"s3://{s3_bucket}", f"{local_s3_dir}"]), shell=True)
        
        if out.returncode != 0:
            print(f"Something went wrong when using the `aws` command!")
            exit(out.returncode)

    @staticmethod
    def main(args):

        config = args.config

        if args.sync_from_s3:
            InboxCommand.sync_from_s3(config)

        InboxCommand.summarize(config, args)