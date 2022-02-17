#!/usr/bin/env python3
""" Module of Session Auth views
"""

from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - session response json with cookie
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    obj_list = User.search({"email": email})
    if not obj_list:
        return jsonify({"error": "no user found for this email"}), 404
    for i in range(len(obj_list)):
        if User.is_valid_password(obj_list[i], password):
            from api.v1.app import auth      # WARNING with circular import
            session = jsonify(obj_list[i].to_json())
            session.set_cookie(
                getenv("SESSION_NAME", None),
                auth.create_session(obj_list[i].id)
            )
            return session
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def auth_session_logout() -> str:
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    return jsonify({}), 200
