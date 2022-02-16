#!/usr/bin/env python3
""" Module of basic authentication
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """BasicAuth - empty class by now"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """extract_base64_authorization_header - return base from header"""
        if authorization_header is None or \
                type(authorization_header) != str or \
                authorization_header[:6] != "Basic ":
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header - returns decoded string"""
        if base64_authorization_header is None or \
                type(base64_authorization_header) != str:
            return None
        try:
            base64_message = base64_authorization_header
            base64_bytes = base64_message.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('utf-8')
            return message
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """extract_user_credentials - returns credential in a tuple"""
        if decoded_base64_authorization_header is None or \
                type(decoded_base64_authorization_header) != str or \
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        credentials = decoded_base64_authorization_header.split(':')
        return tuple(credentials)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """user_object_from_credentials - retrieve user info"""
        if user_email is None or type(user_email) != str or \
                user_pwd is None or type(user_pwd) != str:
            return None
        try:
            obj_list = User.search({"email": user_email})
            if not obj_list:
                return None
            for i in range(len(obj_list)):
                if User.is_valid_password(obj_list[i], user_pwd):
                    return obj_list[i]
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user - return a user object using request"""

        a = self.authorization_header(request)
        auth_header = self.extract_base64_authorization_header(a)
        decoded_header = self.decode_base64_authorization_header(auth_header)
        user_cred = self.extract_user_credentials(decoded_header)
        user_obj = self.user_object_from_credentials(user_cred[0], user_cred[1])
        return user_obj
