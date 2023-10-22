#!/usr/bin/python3
"""list all states and show them on template"""


from flask import Flask, render_template
from models import *
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def listStates():
    """list of states"""
    states = storage.all(State)

    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear_db():
    """close engine"""
    return storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
