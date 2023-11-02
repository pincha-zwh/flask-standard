from dataclasses import dataclass, asdict

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

from configuration import Config, DevelopmentConfig


@dataclass
class APIResponse(object):
    code: int = 500
    message: str = "server failed"
    description: str = ""

    def to_dict(self):
        return asdict(self)

    def jsonify(self):
        """return json format to request"""
        return jsonify(self.to_dict())


def handler_error_request(e):
    """handler flask all error"""
    api_response = APIResponse()
    if isinstance(e, HTTPException):
        api_response.code = e.code
        api_response.message = e.name
        api_response.description = e.description

    return api_response.jsonify()


def handler_before_request():
    """handler before request"""
    pass


def handler_after_request(resp=None):
    """handler after request"""

    return resp


def create_app(config: Config):
    """create application for flask"""

    # create flask object and loading config by args config
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    @app.errorhandler(HTTPException)
    def handler_http_error(e):
        return handler_error_request(e)

    @app.errorhandler
    def handler_error(e):
        return handler_error_request(e)

    @app.before_request
    def before_request():
        return handler_before_request()

    @app.after_request
    def after_request(resp):
        return handler_after_request(resp)

    return app


app = create_app(
    config=DevelopmentConfig()
)
