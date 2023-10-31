from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route("/")
def input_validate():

    integer = request.args.get('input', '')

    # check if input is valid integer
    try:

        # output = GET req to increment.py, through gateway
        # debug as printing the number until figuring out proper GET req

        int(integer)
        
        output = integer
        output_status = 200

    except ValueError:
        
        output = "<p>Invalid input</p>"
        output_status = 400

    return Response(response=output, status=output_status)
