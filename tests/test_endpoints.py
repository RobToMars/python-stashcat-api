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
        raise Exception("Endpoint.s with error")


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


def test_account_endpoint_availability():
    account_endpoint_methods = {
        messenger.account.change_email: None,
        messenger.account.change_password: None,
        messenger.account.change_status: None,
        messenger.account.deactivate_device: None,
        messenger.account.delete: None,
        messenger.account.list_active_devices: None,
        messenger.account.muted: None,
        messenger.account.settings: None,
        messenger.account.toggle_device_notifications: None,
        messenger.account.toggle_notifications: None,
        messenger.account.toggle_online_status: None,
        messenger.account.toggle_read_status: None
    }
    _test_availability(account_endpoint_methods)


def test_channels_endpoint_availability():
    channels_endpoint_methods = {
        messenger.channels.addModeratorStatus: None,
        messenger.channels.availableInvites: None,
        messenger.channels.changePermissions: None,
        messenger.channels.confirmMembershipRequest: None,
        messenger.channels.create: None,
        messenger.channels.createInvite: None,
        messenger.channels.declineMembershipRequest: None,
        messenger.channels.delete: None,
        messenger.channels.edit: None,
        messenger.channels.editDescription: None,
        messenger.channels.editPassword: None,
        messenger.channels.encryptionUpgradeAvailable: None,
        messenger.channels.files: None,
        messenger.channels.info: None,
        messenger.channels.join: None,
        messenger.channels.members: None,
        messenger.channels.quit: None,
        messenger.channels.recommendations: None,
        messenger.channels.removeModeratorStatus: None,
        messenger.channels.removeUser: None,
        messenger.channels.rename: None,
        messenger.channels.setUserWritePermissions: None,
        messenger.channels.subscripted: None,
        messenger.channels.upgradeChannelEncryption: None,
        messenger.channels.visible: None
    }
    _test_availability(channels_endpoint_methods)
