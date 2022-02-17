#!/usr/bin/env python3
""" Module of session authentication
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64
import uuid


class SessionAuth(Auth):
    """BasicAuth - empty clas by now"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create_session - create session ID for a user_id"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session_id - returns user_id from session_id"""
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """current_user - return user_id from request"""
        s_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(s_cookie)
        return User.get(user_id)
