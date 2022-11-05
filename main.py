# Flask in python
# To run the api, on your terminal do: export FLASK_APP=main(main is the name of the python file)
# adn flask --app main run
from flask import Flask, request, jsonify
import os
import openai
from openai.api_resources import completion

openai.api_key = os.getenv("OPENAI_API_KEY")

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
    else:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=data["operation_type"],
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        try:
            response = response.choices[0].text
            result = response.split("=")[-1].strip()
        except:
            result = response.choices[0].text


    return jsonify({"slackUsername": "Hassan Aleeyah", "operation_type": data["operation_type"], "result": result})
