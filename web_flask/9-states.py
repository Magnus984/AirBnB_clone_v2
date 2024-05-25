#!/usr/bin/python3
"""Starts a Flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def states_page(id=None):
    states = storage.all(State)
    if id is not None:
        state_id = 'State.' + id
    return render_template(
            "9-states.html",
            states=states, state_id=state_id
            )


@app.teardown_appcontext
def remove_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
