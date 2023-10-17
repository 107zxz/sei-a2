from flask import Flask
from flask import request
import json
import random

app = Flask(__name__)

random.seed()

jokes = json.load(open("jokes.json"))

@app.route("/")
def status_msg():
    return "Use /joke to get a random joke"

@app.route("/joke")
def get_joke():
    return random.choice(jokes)
