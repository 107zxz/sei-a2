from flask import Flask
from flask import Response
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def timestamp():

    current_datetime = datetime.now()
    current_datetime_formatted = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    output = f"<p>The current date and time is: <b>{current_datetime_formatted}</b>.</p>"

    output_status = 200

    return Response(response=output, status=output_status)

