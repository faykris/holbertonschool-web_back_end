#!/usr/bin/env python3
"""
User definition file
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """User - class"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, " + \
            f"email='{self.email}', " + \
            f"hashed_password='{self.hashed_password}', " + \
            f"session_id='{self.hashed_password}', " + \
            f"reset_token='{self.reset_token}')>'"
