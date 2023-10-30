from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def status_msg():
    return "<p>Use /increment?input=[integer] to increment an integer input</p>"

@app.route("/increment")
def input_validate():

    integer = request.args.get('input', '')

    # check if input is valid integer
    if integer.isdigit():

        # output = GET req to increment.py, through gateway
        # debug as printing the number until figuring out proper GET req
        output = integer

    else:
        output = "<p>Invalid input</p>"

    return output
