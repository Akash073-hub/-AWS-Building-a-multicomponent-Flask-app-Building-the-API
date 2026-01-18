from flask import Flask, request, Response
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello from Gateway!'


@app.route('/items', methods=['GET'])
# TODO: add a route for GET with item id
def get_devicess(item_id=None):
    return 'Hello from GET'


# TODO: add a route for DELETE
def delete_device(item_id):
    return 'Hello from DELETE'


# TODO: add a route for POST
def post_device():
    return 'Hello from POST'


# TODO: add a route for PUT
def put_device(item_id):
    return 'Hello from PUT'


if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
