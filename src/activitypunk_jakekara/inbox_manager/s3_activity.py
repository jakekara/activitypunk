import json
from activitypunk_jakekara.inbox_manager.activity import Activity
from requests import Request


class S3Activity(Activity):

    def __init__(self, s3_file_contents:str):

        s3_file_object = json.loads(s3_file_contents)
        request = Request()

        request.headers = s3_file_object["headers"]
        request.body = s3_file_object["body"]
        super().__init__(request=request)