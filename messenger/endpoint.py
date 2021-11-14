# -*- coding: UTF-8 -*-# enable debugging

"""
Endpoint
"""

# Built-in Python library
from typing import Union, Callable


class Endpoint:

    middleware = set()
    endpoints = set()

    @classmethod
    def __init_subclass__(cls, **kwargs):
        cls.middleware.update(cls.__name__)

    @classmethod
    def add_end_point(cls, end_point):
        # TODO: Register all endpoints during loading of the modules
        if end_point not in cls.endpoints:
            cls.endpoints.update(end_point)
            print(f"Added endpoint: {end_point}")


def endpoint(func: Union[classmethod, staticmethod, Callable]) -> Callable:
    def wrapper(instance, *args, **kwargs):
        end_point = f"/{instance.name}/{func.__name__}"
        Endpoint.add_end_point(end_point)
        response = instance.messenger.post(end_point=end_point)

        assert callable(func), f"{func.__name__} needs to be callable in order to be wrapped by endpoint"

        return func(instance, *args, response=response, **kwargs)

    return wrapper
