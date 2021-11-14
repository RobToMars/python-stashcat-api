# -*- coding: UTF-8 -*-# enable debugging

"""
Account endpoints:
/account/change_email
/account/change_password
/account/change_status
/account/deactivate_device
/account/delete
/account/list_active_devices
/account/muted
/account/settings
/account/toggle_device_notifications
/account/toggle_notifications
/account/toggle_online_status
/account/toggle_read_status
"""

# Package Python library
from messenger.endpoint import Endpoint, endpoint


class Account(Endpoint):
    def __init__(self, messenger):
        self.name = "account"
        self.messenger = messenger

    @endpoint
    def change_email(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")

    @endpoint
    def change_password(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")

    @endpoint
    def change_status(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")

    @endpoint
    def deactivate_device(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")

    @endpoint
    def delete(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")

    @endpoint
    def list_active_devices(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")

    @endpoint
    def muted(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")

    @endpoint
    def settings(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")

    @endpoint
    def toggle_device_notifications(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")

    @endpoint
    def toggle_notifications(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")

    @endpoint
    def toggle_online_status(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")

    @endpoint
    def toggle_read_status(self, response):
        # TODO + JSONError: no credentials submitted
        print(f"Response: {response}")
