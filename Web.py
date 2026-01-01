from flask import Flask

app = Flask(__name__)

with open("Da-ggle.html", mode="r") as d:
    html = d.read()

with open("robot_s.txt", mode="r") as r:
    robots = r.read()

@app.route("/")
def web():
    return html

@app.route("/robots.txt")
def robo():
    return robots

if __name__ == "__main__":
    app.run()

