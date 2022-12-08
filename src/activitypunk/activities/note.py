from activitypunk.actor import ActivityPubActor
from activitypunk.utils.time import isonow
from hashlib import md5

def note(sender: ActivityPubActor, message):

    now = isonow()
    hash_str = md5((now + message).encode()).hexdigest()
    message_id = sender.webfinger.actor_url + "#" + hash_str

    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
        ],
        "type": "Create",
        "actor": sender.webfinger.actor_url,
        "published": now,
        "to": [
            # AS-public,
            # sender followers
        ],
        "cc": [],
        "object": {
            "type": "Note",
            "id": message_id,
            "published": now,
            "attributedTo": sender.webfinger.actor_url,
            "to": [
                # AS-public,
                # sender followers
            ],
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