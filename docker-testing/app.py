from flask import Flask
from flask import request
from time import sleep
import random

app = Flask(__name__)

random.seed()

@app.route("/")
def status_msg():
    return "<p>Use /loss?url=[link] to detect if the passed link contains a 'loss' joke</p>"

@app.route("/loss")
def get_joke():

    if request.args.get('url', '') == '':
        return "<p>Invalid link.</p><p>Use /loss?url=[link] to detect if the passed link contains a 'loss' joke</p>"

    sleep(random.randrange(3, 7))
    return """
    <p>The passed url contains <b>{}</b> 'Loss' jokes.</p><p>You are in grave danger.</p>
    """.format(random.randint(2048, 8192))
