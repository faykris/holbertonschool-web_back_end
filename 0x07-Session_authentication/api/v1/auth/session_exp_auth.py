#!/usr/bin/env python3
""" Module of session expiration
"""
from datetime import datetime, timedelta

from api.v1.auth.session_auth import SessionAuth
from os import getenv


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""

    def __init__(self):
        """constructor method"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION', 0))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """create_session"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user_id_for_session_id"""
        if session_id is None:
            return None
        if not self.user_id_by_session_id.get(session_id):
            return None
        user_id = self.user_id_by_session_id[session_id].get('user_id')
        create_at = self.user_id_by_session_id[session_id].get('created_at')
        if self.session_duration <= 0:
            return user_id
        if not create_at:
            return None
        if create_at + timedelta(
                seconds=self.session_duration) < datetime.now():
            return None
        return user_id
