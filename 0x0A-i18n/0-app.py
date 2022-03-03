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
    return


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
