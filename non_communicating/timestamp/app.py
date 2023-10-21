from flask import Flask
from flask import request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def status_msg():
    return "<p>Use /timestamp to get the current date and time.</p>"

@app.route("/timestamp")
def timestamp():

    current_datetime = datetime.now()
    current_datetime_formatted = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    output = "<p>The current date and time is: <b>{}</b>.</p>"

    return output.format(current_datetime_formatted)

