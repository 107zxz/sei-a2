from flask import Flask
from flask import Response
import random

app = Flask(__name__)
random.seed()

@app.route("/")
def dice_roll():

    random_int = random.randint(1, 6)
    output = f"<p>You rolled a <b>{random_int}</b>.</p>"
    output_status = 200

    return Response(response=output, status=output_status)
