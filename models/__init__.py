from dataclasses import dataclass, asdict

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class BaseModel(object):

    def to_dict(self):
        """to simple dict"""
        raise NotImplementedError(f"{self.__class__.__name__} not implemented to_dict function")
