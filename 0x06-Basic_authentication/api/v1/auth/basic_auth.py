#!/usr/bin/env python3
""" Module of basic authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth - empty class by now"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        if authorization_header is None or \
                type(authorization_header) != str or \
                authorization_header[:6] != "Basic ":
            return None
        return authorization_header.split()[1]
