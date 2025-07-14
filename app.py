from flask import Flask

app = Flask(__name__)


@app.route("/home)"
def home():
    return "API IS RUNNING PERFECTLY ..."

@app.route("/abhijeet")
def abhijeet()
    return "Created by Abhijeet"

run(host = "0.0.0.0.", port = 5000)






