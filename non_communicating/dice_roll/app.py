from flask import Flask
from flask import request
import random

app = Flask(__name__)
random.seed()

@app.route("/")
def status_msg():
    return "<p>Use /dice_roll to roll a dice from 1 to 6.</p>"

@app.route("/dice_roll")
def dice_roll():

    random_int = random.randint(1, 6)
    output = "<p>You rolled a <b>{}</b>.</p>"

    return output.format(random_int)
