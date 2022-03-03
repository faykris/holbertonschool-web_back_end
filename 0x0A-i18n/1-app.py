#!/usr/bin/env python3
"""1. Basic Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = "en"
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
babel = Babel(app)


class Config(object):
    """Config"""
    LANGUAGES = ["en", "fr"]

    @babel.localeselector
    def get_locale():
        """get_locale"""
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ GET
    Return:
      - rendered HTML template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
