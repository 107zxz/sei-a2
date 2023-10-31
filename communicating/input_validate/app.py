from flask import Flask
from flask import request
from flask import Response

import requests

app = Flask(__name__)

@app.route("/")
def input_validate():

    integer = request.args.get('input', '')

    # check if input is valid integer
    try:
        integer = int(integer)
    except ValueError:
        return Response(response="<p>Invalid input</p>", status=400)

    # get incremented value
    incremented = requests.get("http://calculate-service:5000", params={"input": integer}).content

    # Return formatted value
    return requests.get("http://format-output-service:5000", params={"input": incremented}).content
