#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from markupsafe import escape
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def no_hello():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route(
        "/python/",
        defaults={'text': 'is cool'},
        strict_slashes=False
        )
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    return "Python {}".format(escape(text.replace('_', ' ')))


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    return f'{escape(n)} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def first_template(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
