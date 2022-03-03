#!/usr/bin/env python3
"""0. Basic Flask app"""
from flask import Flask, jsonify
from flask_babel import Babel

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def status() -> str:
    """ GET 
    Return:
      - the status of the API
    """
    pass
