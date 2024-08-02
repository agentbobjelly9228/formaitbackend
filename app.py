from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def sendToLLM(data):
    pass


def formatPDF():
    file = "paper.pdf"


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "What is up there my friend"


app.run(debug=True)
