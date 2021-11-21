# -*- coding: UTF-8 -*-# enable debugging

"""
Logger
"""

# Built-in Python library
import logging
import http.client


def set_logger(level=logging.DEBUG) -> logging.Logger:
    formatting = "%(asctime)s %(levelname)s %(name)s %(module)s.%(funcName)s:%(lineno)d - %(message)s"
    logging.basicConfig(format=formatting)
    logger = logging.getLogger()
    logger.setLevel(level)

    if level == logging.DEBUG:
        http.client.HTTPConnection.debuglevel = 1

    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.propagate = True
    requests_log.setLevel(level)

    return logger
