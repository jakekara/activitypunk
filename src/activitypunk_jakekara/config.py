import os
import configparser
from logging import getLogger


logger = getLogger(__name__)

class ActivityPunkConfig:

    """"""

    # API properties
    actor=None
    private_key=None
    public_key=None
    user_at_host=None
    data_dir=None


    # Internal stuff
    DEFAULT_CONFIG_DIR=os.path.expanduser("~/.activitypunk/")
    DEFAULT_CONFIG_FILE_PATH=os.path.join(DEFAULT_CONFIG_DIR, "config")
    DEFAULT_PRIVATE_KEY_PATH=os.path.join(DEFAULT_CONFIG_DIR, "private.pem")
    DEFAULT_PUBLIC_KEY_PATH=os.path.join(DEFAULT_CONFIG_DIR, "public.pem")
    DEFAULT_DATA_DIR=os.path.join(DEFAULT_CONFIG_DIR, "data")
    DEFAULT_PROFILE_NAME="default"


    def __init__(self, config_file_path=DEFAULT_CONFIG_FILE_PATH, profile_name=DEFAULT_PROFILE_NAME):
        self._config_file_path = config_file_path
        self._profile_name = profile_name
        self._config = configparser.ConfigParser()
        self.load_profile()

    def load_profile(self):

        self._config.read(self._config_file_path)

        if self._profile_name not in self._config.sections():
            logger.warn(f"Did not find profile {self._profile_name} in {self._config.sections()}")
            return

        props = self._config[self._profile_name]

        self.actor = props.get("actor")
        self.private_key_file_path = os.path.expanduser(props.get("private_key_file", self.DEFAULT_PRIVATE_KEY_PATH))
        self.public_key_file_path = os.path.expanduser(props.get("public_key_file", self.DEFAULT_PUBLIC_KEY_PATH))
        self.user_at_host = props.get("user_at_host")
        self.s3_bucket = props.get("s3_bucket")
        self.data_dir = os.path.expanduser(props.get("data_dir", self.DEFAULT_DATA_DIR))
        
        try:
            self.private_key = open(self.private_key_file_path).read()
        except FileNotFoundError:
            logger.warn(f"Private key not found: {self.private_key_file_path}")


        try: 
            self.public_key = open(self.public_key_file_path).read()
        except FileNotFoundError:
            logger.warn(f"Public key not foind: {self.public_key_file_path}")

