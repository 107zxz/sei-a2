from flask import Flask
from flask import request
import random

app = Flask(__name__)
random.seed()

@app.route("/")
def dice_roll():

    random_int = random.randint(1, 6)
    output = "<p>You rolled a <b>{}</b>.</p>"

    return output.format(random_int)
