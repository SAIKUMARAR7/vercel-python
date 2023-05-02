from flask import Flask
from art import *
from art import tprint


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/about")
def about():
    return "About"


@app.route("/art")
def art_api():
    return tprint("art")

@app.route("/test")
def test():
    return "Hello, All"
