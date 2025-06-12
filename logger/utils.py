# utils.py

import getpass
from datetime import datetime

def get_username():
    return getpass.getuser()

def get_timestamp():
    return datetime.now().isoformat()