from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def status_msg():
    return "<p>Use /greetings to get a welcome message.</p>"

@app.route("/greetings")
def greetings():

    output = """
    <p>Welcome to the <b>Kubernetes</b> microservice gateway architecture!</p>
    <p>This system was set up with the help of <b>Kubernetes</b>, <b>Docker</b> and <b>Flask</b>, hope you enjoy your stay!</p>
    <p>Available microservices:</p>
    <ul>
        <li>a</li>
        <li>b</li>
        <li>c</li>
    </ul> 
    """

    return output

