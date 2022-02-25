#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, abort, request, redirect
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """welcome - test"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """register_user"""
    try:
        user = AUTH.register_user(
            request.form['email'],
            request.form['password']
        )
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """login - make user login"""
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        session = jsonify({"email": email, "message": "logged in"})
        session.set_cookie("session_id", AUTH.create_session(email))
        return session
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """logout"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
