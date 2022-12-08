from enum import Enum

import urllib3


class UserStringTypes(Enum):
    USER_ONLY = 1
    USER_AT_HOST = 2
    ACTOR_URI = 3
    INVALID_FORMAT = 4


def determine_user_string_type(raw_str):
    """
    Determine if a string is a USER_AT_HOST or ACTOR_URI. Raise ValueError otherwise
    """

    if "@" in raw_str:
        return UserStringTypes.USER_AT_HOST
    
    try:
        url = urllib3(raw_str)
        return UserStringTypes.ACTOR_URI
    except:
        pass

    return UserStringTypes.INVALID_FORMAT