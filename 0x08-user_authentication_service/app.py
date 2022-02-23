#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, abort, request
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """welcome - test"""
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
