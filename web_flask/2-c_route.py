#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask

app = Flask(__name__)

# Route to display "Hello HBNB!" when the root URL is accessed


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'

# Route to display "HBNB" when the /hbnb URL is accessed


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'

# Route to display "C <text>" when /c/<text> URL is accessed


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays 'C <text>'"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    # Runs the Flask application on 0.0.0.0:5000 without debug mode
    app.run(host="0.0.0.0", port=5000, debug=False)
