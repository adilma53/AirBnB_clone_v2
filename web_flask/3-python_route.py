#!/usr/bin/python3
"""python_route"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hellow():
    """simple server test"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """simple server test returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """c route"""
    noUnderScore = text.split('_')
    joined = ' '.join(noUnderScore)
    return f'C {joined}'


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """python route"""
    noUnderScore = text.split('_')
    joined = ' '.join(noUnderScore)
    return f'Python {joined}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
