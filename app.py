from flask import Flask
from werkzeug.exceptions import HTTPException

from api.api_user import api_user
from common.resp import APIResponse
from configuration import Config, DevelopmentConfig
from exceptions.service_exception import ServiceException


def handler_error_request(e):
    """handler flask all error"""
    api_response = APIResponse()

    if isinstance(e, ServiceException):
        # service failed
        api_response.code = e.code
        api_response.message = str(e)
        api_response.description = ""
    elif isinstance(e, HTTPException):
        # http origin failed
        api_response.code = e.code
        api_response.message = e.name
        api_response.description = e.description
    else:
        api_response.code = 500
        api_response.message = "service exception"
        api_response.description = ""

    return api_response.make_failed()


def handler_before_request():
    """handler before request"""
    pass


def handler_after_request(resp=None):
    """handler after request"""

    return resp


def loading_blueprint_api(current_app: Flask):
    """loading api routers"""
    current_app.register_blueprint(api_user, url_prefix="/api/user/")


def create_app(config: Config):
    """create application for flask"""

    # create flask object and loading config by args config
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    # loading blueprint for api
    loading_blueprint_api(current_app=app)

    @app.errorhandler(Exception)
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
