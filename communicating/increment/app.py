from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def increment():

    integer = request.args.get('input', '')

    integer_inc = int(integer) + 1

    return str(integer_inc)
