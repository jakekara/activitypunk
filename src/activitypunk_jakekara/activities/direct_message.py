from activitypunk_jakekara.actor import ActivityPubActor
from activitypunk_jakekara.utils.time import isonow
from hashlib import md5

def direct_message(sender: ActivityPubActor, recipient: ActivityPubActor, message):

    now = isonow()
    hash_str = md5((now + recipient.webfinger.actor_url + message).encode()).hexdigest()
    message_id = sender.webfinger.actor_url + "#" + hash_str

    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
        ],
        "type": "Create",
        "actor": sender.webfinger.actor_url,
        "published": now,
        "to": [recipient.webfinger.actor_url],
        "cc": [],
        "object": {
            "type": "Note",
            "id": message_id,
            "published": now,
            "attributedTo": sender.webfinger.actor_url,
            "to": [recipient.webfinger.actor_url],
            "cc": [],
            "content": message,
            "tag": [
                {
                    "type": "Mention",
                    "href": recipient.webfinger.actor_url,
                    "name": f"@{recipient.webfinger.user.user}@{recipient.webfinger.user.host}"
                }
            ]
            }
        }