from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/amit")
def greet_sonal():
    return "<p>Sonal i love you</p>"