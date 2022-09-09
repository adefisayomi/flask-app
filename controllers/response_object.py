

from typing import Dict


class Response:
    __slots__ = ["message", "success", "data"]

    def __init__(self, message, success, data):
        self.success = success
        self.message = message
        self.data = data

    def res(self):
        return ({
            "success": self.success,
            "message": self.message,
            "data": self.data
        })