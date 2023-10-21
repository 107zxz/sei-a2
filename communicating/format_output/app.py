from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def format_output():

    integer = request.args.get('input', '')

    output = "<p>Your result is: <b>{}</b>.</p>"
    return output.format(integer)

