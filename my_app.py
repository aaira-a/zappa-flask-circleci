import datetime
import logging
import os

from flask import Flask, request

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "hello world"


@app.route("/status", methods=['POST'])
def status():
    name = request.form.get("name")
    status = request.form.get("status")
    return (f"hi {name}, it's {status}!")


@app.route("/envvar", methods=['GET'])
def envvar():
    return os.environ["ENV_VAR_1"]


def scheduled():
    mydatetime = datetime.datetime.utcnow()
    mystring = (f"schedule triggered on {mydatetime}")
    logger.info(mystring)
    return mystring


if __name__ == "__main__":
    app.run()
