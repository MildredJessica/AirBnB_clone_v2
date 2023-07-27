#!/usr/bin/python
"""Script that starts a Flask web application
    /
    /hbnb
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return ("HBNB!")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
