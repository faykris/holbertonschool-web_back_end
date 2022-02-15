#!/usr/bin/env python3
""" Module of basic authentication
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """BasicAuth - empty class by now"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """extract_base64_authorization_header - return base"""
        if authorization_header is None or \
                type(authorization_header) != str or \
                authorization_header[:6] != "Basic ":
            return None
        return authorization_header.split()[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header"""
        if base64_authorization_header is None or \
                type(base64_authorization_header) != str:
            return None
        try:
            base64_message = base64_authorization_header
            base64_bytes = base64_message.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('utf-8')
            return message
        except:
            return None
