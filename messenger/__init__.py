# -*- coding: UTF-8 -*-# enable debugging

"""
Messenger
"""

# Built-in Python library
import json
import logging

# External Python library
import requests

# Package Python library
from messenger.auth import Auth
from messenger.account import Account


class JSONError(Exception):
    pass


class Messenger:
    version = "4.8.0"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    }

    def __init__(self, *, root_endpoint: str = "https://api.stashcat.com"):
        self.root_endpoint = root_endpoint
        self.auth = Auth(self)
        self.account = Account(self)

    def post(self, end_point: str, data=None, json_data=None, headers: dict = None, raise_for_status: bool = True):
        if headers is None:
            headers = {}
        headers.update(self.headers)

        url = f"{self.root_endpoint}{end_point}"
        response = requests.post(url, data=data, json=json_data, headers=headers)

        if raise_for_status:
            response.raise_for_status()

        json_content = response.json()

        if raise_for_status and json_content.get("status") and json_content.get("status").get("value"):
            status = json_content.get("status")
            if status.get("value").upper() != "OK":
                message = status.get("message", "")
                raise JSONError(f"Response to {url}: {message}")

        json_content = json_content.get("payload", json_content)

        logging.debug(json.dumps(json_content, indent=2))

        return json_content
