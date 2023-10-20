from flask import Flask
from flask import request

app = Flask(__name__)

# idk if need status_msg() if its not going to be directly accessed?
@app.route("/")
def increment():

    integer = request.args.get('input', '')
    integer_inc = integer + 1

    # output = GET req to format_output, through gateway
    output = integer_inc

    return output

