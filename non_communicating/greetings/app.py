from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def greetings():

    output = """
    <p>Welcome to the <b>Kubernetes</b> microservice gateway architecture!</p>
    <p>This system was set up with the help of <b>Kubernetes</b>, <b>Docker</b> and <b>Flask</b>, hope you enjoy your stay!</p>
    <p>Available microservices:</p>
    <ul>
        <li>comm/increment?input=[integer] to increment an integer input.</li>
        <li>noncomm/greetings: Print this welcome message.</li>
        <li>noncomm/dice_roll: Roll a dice from 1 to 6.</li>
        <li>noncomm/timestamp: Get the current date and time.</li>
    </ul> 
    """

    return output

