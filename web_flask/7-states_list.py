#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_state():
    state_objects = []
    for state in storage.all(State).values():
        state_objects.append(state)
    state_objects = sorted(state_objects, key=lambda state: state.name)
    return render_template(
            "7-states_list.html", state_objects=state_objects
            )


@app.teardown_appcontext
def remove_session(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
