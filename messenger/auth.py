# -*- coding: UTF-8 -*-# enable debugging

"""
Auth

Endpoints:
/auth/check
/auth/login
/auth/logout
/auth/method
/auth/reset_password
/auth/get_server_config
"""

# Package Python library
from messenger.endpoint import Endpoint, endpoint


class Auth(Endpoint):
    def __init__(self, messenger):
        self.name = "auth"
        self.messenger = messenger

    @endpoint
    def check(self, response):
        # TODO
        # JSONError: missing values, device_id und client_key required
        print(f"Response: {response}")

    @endpoint
    def login(self, response):
        # TODO
        # JSONError: missing values, credentials and app data required
        print(f"Response: {response}")

    @endpoint
    def logout(self, response):
        # TODO
        # JSONError: missing values, device_id required
        print(f"Response: {response}")

    @endpoint
    def method(self, response):
        # TODO
        # JSONError: email is required
        print(f"Response: {response}")

    @endpoint
    def reset_password(self, response):
        # TODO
        # JSONError: missing values, email is required and has to be valid
        print(f"Response: {response}")

    @endpoint
    def get_server_config(self, response):
        # TODO
        print(f"Response: {response}")
