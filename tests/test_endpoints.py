# -*- coding: UTF-8 -*-# enable debugging

"""
Test availability of endpoints
"""

# Built-in Python library
import time

# Package Python library
from messenger import Messenger, JSONError
from messenger.logger import set_logger


logger = set_logger("DEBUG")
messenger = Messenger()


def _test_availability(endpoint_methods):

    passed = {"verdict": True, "message": ""}
    errors = False
    for endpoint_method in endpoint_methods:
        try:
            endpoint_method()
            endpoint_methods[endpoint_method] = passed

        except JSONError as err:
            logger.info(f"{endpoint_method}: {err}")
            endpoint_methods[endpoint_method] = {"verdict": True, "message": str(err)}

        except Exception as err:
            logger.exception(f"{endpoint_method}: {err}")
            errors |= True
            endpoint_methods[endpoint_method] = {"verdict": True, "message": str(err)}

        time.sleep(0.5)  # Do not flood API

    if errors:
        raise Exception("Endpoint/s with error")


def test_auth_endpoint_availability():
    auth_endpoint_methods = {
        messenger.auth.check: None,
        messenger.auth.login: None,
        messenger.auth.logout: None,
        messenger.auth.method: None,
        messenger.auth.reset_password: None,
        messenger.auth.get_server_config: None
    }
    _test_availability(auth_endpoint_methods)
