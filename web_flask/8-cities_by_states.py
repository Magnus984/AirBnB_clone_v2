#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
import os


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    state_objects = []
    for state in storage.all(State).values():
        state_objects.append(state)
    state_objects = sorted(state_objects, key=lambda state: state.name)
    return render_template(
            "8-cities_by_states.html", state_objects=state_objects
            )


@app.teardown_appcontext
def remove_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
