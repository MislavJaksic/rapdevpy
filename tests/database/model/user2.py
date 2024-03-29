from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base2


class User2(Base2):
    __tablename__ = "user_account_2"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address2", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
