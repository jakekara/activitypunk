
import json


class Request:

    body:str = None
    headers:dict = None

class Activity:

    def __init__(self, request:Request):
        self.request = request
        self.activity_pub_body = json.loads(request.body)

    def __str__(self):
        return self.activity_pub_body["id"] + ": " + self.activity_pub_body["type"]

   
        

