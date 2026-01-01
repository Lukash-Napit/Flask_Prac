from flask import Flask

app = Flask(__name__)

with open("Da-ggle.html", mode="r") as d:
    html = d.read()

@app.route("/")

def web():
    return html
