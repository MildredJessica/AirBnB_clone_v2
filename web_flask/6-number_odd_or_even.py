#!/usr/bin/python
"""Script that starts a Flask web application
    /
    /hbnb
    /c/<text>
    /python/(<text>)
    /number/<n>
    /number_template/<n>
    /number_odd_or_even/<n>
"""

from flask import Flask
from flask import render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display n is a number only if n is an integer"""
    return ("{:d} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display HTML page only if n is an integer"""
    return (render_template('5-number.html', n=n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Display HTML page only if n is an integer"""
    return (render_template('6-number_odd_or_even.html', n=n))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
