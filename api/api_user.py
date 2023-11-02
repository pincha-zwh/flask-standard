from flask import Blueprint

from exceptions.service_exception import NotFundResourceException, ParamsException

api_user = Blueprint("api_user", __name__)

USERS = [
    dict(id=1, username="pincha.zwh", email="pincha.zwh@gmail.com"),
    dict(id=2, username="zwhset", email="zwhset@163.com"),
]


@api_user.route("/")
def list_user():
    """list user"""
    return USERS


@api_user.route('/<int:user_id>/')
def get_user(user_id: int):
    """get user by user_id"""
    # check user id
    if user_id <= 0:
        raise ParamsException(f"params user_id failed")

    user = None
    for db_user in USERS:
        db_user_id = db_user.get("id", None)
        if db_user_id == user_id:
            user = db_user
            break
    if user is None:
        # not fund user by user_id
        raise NotFundResourceException(f"not fund user {user_id}")

    return user
