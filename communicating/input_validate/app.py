from flask import Flask
from flask import request

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

    except ValueError:
        
        output = "<p>Invalid input</p>"

    return output
