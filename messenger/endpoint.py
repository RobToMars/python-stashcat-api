# -*- coding: UTF-8 -*-# enable debugging

"""
Endpoint
"""

# Built-in Python library
from typing import Union, Callable


class Endpoint:
    name = ""
    children = []

    @classmethod
    def __init_subclass__(cls):
        if issubclass(cls, Endpoint):
            cls.children = []
            cls.__base__.children.append(cls)
        else:
            raise NotImplementedError

    @classmethod
    def get_endpoint(cls):
        parent = ""
        if issubclass(cls.__base__, Endpoint):
            parent = cls.__base__.get_endpoint()

        if cls.name:
            return f"{parent}/{cls.name}"
        else:
            return f"{parent}"

    def __init__(self, **kwargs):
        self.endpoint = self.get_endpoint()
        self.root = kwargs.get("root", self)
        self.messenger = kwargs.get("messenger", None)

        for child in self.children:
            instance = child(root=self.root, messenger=self.messenger)
            setattr(self, child.name, instance)

    def __call__(self, *args, **kwargs):
        print(f"{self.endpoint} + {args} + {kwargs}\n")
        response = self.root.messenger.post(*args, endpoint=self.endpoint, **kwargs)
        return self.process_response(response)

    def process_response(self, response):
        raise NotImplementedError


class Auth(Endpoint):
    name = "auth"

    def process_response(self, response):
        print(f"Response {response}")


class GetServerConfig(Auth):
    name = "get_server_config"

    def process_response(self, response):
        print(f"Messenger {self.messenger}")
        print(f"Endpoint {self.root}")
        print(f"Response {response}")
