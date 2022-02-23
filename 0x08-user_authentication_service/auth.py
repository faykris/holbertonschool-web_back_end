#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """_hash_password"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('UTF-8'), salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """constructor - method"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register_user"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = _hash_password(password)
            user = self._db.add_user(email, hashed)
            return user
