#!/usr/bin/python
"""Script that starts a Flask web application
    /
    /hbnb
    /c/<text>
    /python
    /python/<text>
"""

from flask import Flask
import re

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return ("HBNB!")


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Display C followed by the value of the text variable """
    return ("C " + text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Display Python followed by the value of the text variable  is cool"""
    return ("Python " + text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
