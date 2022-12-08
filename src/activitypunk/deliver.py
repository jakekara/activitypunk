"""
Deliver an ActivityPub message to an inbox

This is largely based on a ruby example `deliver.rb` from this blog post:

https://blog.joinmastodon.org/2018/06/how-to-implement-a-basic-activitypub-server/

"""

from datetime import datetime
from time import mktime
import base64
from hashlib import sha256
from wsgiref.handlers import format_date_time
import requests

from activitypunk.actor import ActivityPubFirstPartyActor

def http_date_str():
    now = datetime.now()
    stamp = mktime(now.timetuple())
    date_str = format_date_time(stamp)
    return date_str


def deliver(
    *,
    document,
    inbox_url,
    host, 
    actor: ActivityPubFirstPartyActor
):
    document_digest = "SHA-256=" + base64.b64encode(sha256(document.encode()).digest()).decode()

    date_str = http_date_str()
    
    signed_string = f"(request-target): post /inbox\nhost: {host}\ndate: {date_str}\ndigest: {document_digest}"

    signature = base64.b64encode(actor.sign(signed_string)).decode()

    header = f'keyId="{actor.public_key.id}",headers="(request-target) host date digest",signature="{signature}"'

    response = requests.post(
        inbox_url,
        headers={ 'Host': host, 'Date': date_str, 'Signature': header, 'Digest': document_digest },
        data=document
    )    

    return response