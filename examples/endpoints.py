# -*- coding: UTF-8 -*-# enable debugging

"""
Test endpoints
"""

# Package Python library
from messenger import Messenger
from messenger.logger import set_logger

if __name__ == '__main__':
    set_logger("DEBUG")
    client = Messenger()
    response = client.auth.get_server_config()
    print(response)
