from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from models import db, BaseModel


class User(db.Model, BaseModel):
    """User Domain"""
    # id
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # username
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    # email
    email: Mapped[str] = mapped_column(String(255))

    def to_dict(self):
        data = dict(
            id=self.id,
            username=self.username,
            email=self.email
        )
        return data
