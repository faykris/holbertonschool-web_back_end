#!/usr/bin/env python3
"""1. Basic Babel setup"""
from decimal import localcontext
import locale
from flask import Flask, render_template, request
from flask_babel import Babel, Locale

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config - class"""
    LANGUAGES = ["en", "fr"]
    # BABEL_DEFAULT_LOCALE = "en"
    # BABEL_DEFAULT_TIMEZONE = "UTC"


# app.config.setdefault(Config.BABEL_DEFAULT_LOCALE)
# app.config.setdefault(Config.BABEL_DEFAULT_TIMEZONE)


@app.route('/')
def index():
    """ GET
    Return:
      - rendered HTML template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
