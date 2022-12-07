from activitypunk_jakekara.utils.parsers import UserStringTypes, determine_user_string_type

class User:
    user = None
    host = None

    def __init__(self, *, user, host):
        self.user = user
        self.host = host

    def to_user_at_host(self):
        return f"{self.user}@{self.host}"

    def __str__(self):
        return self.to_user_at_host()

    @staticmethod
    def from_user_at_host(user_at_host:str):
        if determine_user_string_type(user_at_host) != UserStringTypes.USER_AT_HOST:
            raise ValueError("String must be user@host or @user@host")
    
        tmp_string = user_at_host
        if tmp_string.startswith("@"):
            tmp_string = tmp_string[1:]
        parts = tmp_string.split("@")
        parts = tmp_string.split("@")


        if len(parts) != 2:
            raise ValueError("invalid username format. Should be user@host or @user@host")


        return User(user=parts[0], host=parts[1])

