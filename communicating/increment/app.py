from flask import Flask
from flask import request

app = Flask(__name__)

# idk if need status_msg() if its not going to be directly accessed?
@app.route("/")
def increment():

    integer = request.args.get('input', '')

    try:
        integer_inc = int(integer) + 1
        return str(integer_inc)
    except ValueError:
        return "Error: Input is not a number!"
