
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "hello world"


@app.route("/alive", methods=['GET'])
def alive():
    return "it's alive!"


if __name__ == "__main__":
    app.run()
