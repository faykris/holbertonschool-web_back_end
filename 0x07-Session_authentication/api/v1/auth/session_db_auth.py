#!/usr/bin/env python3
""" Module of session database auth
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth - class"""

    def create_session(self, user_id=None):
        """create_session - method"""
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        user_session = UserSession(user_id=user_id, session_id=user_id)
        user_session.save()
        UserSession.save_to_file()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user_id_for_session_id - method"""
        if session_id is None:
            return None
        UserSession.load_from_file()
        users = UserSession.search({'session_id': session_id})
        for user in users:
            if user.create_at + timedelta(
                    seconds=self.session_duration) < datetime.now():
                return None
            return user.user_id

    def destroy_session(self, request=None):
        """destroy_session - method"""
        if not request:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        if self.user_id_by_session_id.get(session_id):
            users = UserSession.search({'session_id': session_id})
            for user in users:
                user.remove()
                UserSession.save_to_file()
                return True
        return False
