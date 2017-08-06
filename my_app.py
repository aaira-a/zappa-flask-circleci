
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "hello world"


@app.route("/status", methods=['POST'])
def status():
    name = request.form.get("name")
    status = request.form.get("status")
    return (f"hi {name}, it's {status}!")


if __name__ == "__main__":
    app.run()
