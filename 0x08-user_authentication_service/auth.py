#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """_hash_password"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('UTF-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """_generate_uuid"""
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """valid_login"""
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                return False
            if bcrypt.checkpw(password.encode('UTF-8'), user.hashed_password):
                return True
            return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """create_session"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """get_user_from_session_id"""
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """destroy_session"""
        self._db.update_user(user_id, session_id=None)
