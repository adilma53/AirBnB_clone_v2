#!/usr/bin/python3
"""Hello HBNB"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """simple server test"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index():
    """returns HBNB"""
    return "HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
