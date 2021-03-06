#!/usr/bin/env python3
""" Module of authentication
"""
from os import getenv
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth - authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth - method"""
        if path is None or excluded_paths is None or \
                len(excluded_paths) == 0:
            return True
        if excluded_paths.__contains__(path) or \
                excluded_paths.__contains__(path + "/"):
            return False
        for ex_path in excluded_paths:
            if path[:ex_path.find('*')] in ex_path[:ex_path.find('*')]:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header - method"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user - method"""
        return None

    def session_cookie(self, request=None):
        """session_cookie - return a cookie value from request"""
        if request is None:
            return None
        return request.cookies.get(getenv('SESSION_NAME', None))
