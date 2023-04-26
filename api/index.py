from flask import Flask
from art import *

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/about")
def about():
    return "About"


@app.route("/art")
def art_api():
    art = text2art("art")
    return art
