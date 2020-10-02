from flask import Flask
from flask import render_template
import os
import sys


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


if __name__ == "__main__":
    app.run(debug=True)
