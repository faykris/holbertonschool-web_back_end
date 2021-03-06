#!/usr/bin/env python3
"""2. Get locale from request"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config(object):
    """Config - class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@babel.localeselector
def get_locale():
    """get_locale - function"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone():
    """get_timezone - function"""
    return Config.BABEL_DEFAULT_TIMEZONE


@app.route('/')
def index():
    """ GET
    Return:
      - rendered HTML template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
