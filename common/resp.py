from dataclasses import dataclass
from typing import Any

from flask import jsonify


@dataclass
class APIResponse(object):
    code: int = 200
    message: str = "Success"
    data: Any = None

    def to_dict(self):
        resp = dict(code=self.code, message=self.message)
        if self.data is not None:
            resp["data"] = self.data

        return resp

    def make_success(self):
        """return json format to request"""
        return jsonify(self.to_dict()), self.code

    def make_failed(self):
        print("failed: ", self.to_dict())
        return jsonify(self.to_dict()), self.code
