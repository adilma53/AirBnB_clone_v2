

#!/usr/bin/python3
"""Hello HBNB"""


from flask import Flask, render_template

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
    """simple server test returns HBNB"""
    noUnderScore = text.split('_')
    joined = ' '.join(noUnderScore)
    return f'C {joined}'


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_tamplate(n):
    """number route with template"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
