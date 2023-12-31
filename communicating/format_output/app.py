from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route("/")
def format_output():

    input = request.args.get('input', '')

    if not input:
        return Response(response="<p>Invalid input</p>", status=400)

    output =  f"<p>Your result is: <b>{input}</b>.</p>"
    output_status = 200

    return Response(response=output, status=output_status)
