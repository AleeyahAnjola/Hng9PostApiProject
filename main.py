# Flask in python
# To run the api, on your terminal do: export FLASK_APP=main(main is the name of the python file)
# adn flask --app main run
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/py")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/getPost", methods=["POST"])
def postapimethod():
    data = request.json
    if data["operation_type"] == "addition":
        result = data["x"] + data["y"]
    elif data["operation_type"] == "subtraction":
        result = data["x"] - data["y"]
    elif data["operation_type"] == "multiplication":
        result = data["x"] * data["y"]

    return jsonify({"slackUsername": "Hassan Aleeyah", "operation_type": data["operation_type"], "result": result})


