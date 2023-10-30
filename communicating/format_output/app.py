from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def format_output():

    text = request.args.get('input', '')

    return "<p>Your result is: <b>{}</b>.</p>".format(text)
