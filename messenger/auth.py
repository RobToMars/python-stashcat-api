# -*- coding: UTF-8 -*-# enable debugging

"""
Auth

Endpoints:
/auth/check
/auth/login
/auth/logout
/auth/method
/auth/oauth
/auth/reset_password
/auth/thirdparty
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
        print(f"Response: {response}")

    @endpoint
    def login(self, response):
        # TODO
        print(f"Response: {response}")

    @endpoint
    def logout(self, response):
        # TODO
        print(f"Response: {response}")

    @endpoint
    def method(self, response):
        # TODO
        print(f"Response: {response}")

    @endpoint
    def oath(self, response):
        # TODO
        print(f"Response: {response}")

    @endpoint
    def reset_password(self, response):
        # TODO
        print(f"Response: {response}")

    @endpoint
    def thirdparty(self, response):
        # TODO
        print(f"Response: {response}")

    @endpoint
    def get_server_config(self, response):
        # TODO
        print(f"Response: {response}")
