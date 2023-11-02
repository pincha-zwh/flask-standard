class ServiceException(Exception):
    """server exception"""
    code: int = 500
    message: str = "service exception"


class NotFundResourceException(ServiceException):
    """not fund resource"""
    code: int = 500
    message: str = "not fund resource"


class ParamsException(ServiceException):
    """params exception"""
    code: int = 400
    message: str = "params exception"
