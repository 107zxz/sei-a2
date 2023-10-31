from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route("/")
def calculate():

    integer = request.args.get('input', '')

    integer_inc = int(integer) + 1

    output = str(integer_inc)
    output_status = 200

    return Response(response=output, status=output_status)
