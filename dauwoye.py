from flask import Flask, render_template, request
from flask_frozen import Freezer

app = Flask(__name__)

freezer = Freezer(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Donate/")
def donate():
    return render_template("donate.html")

@app.route("/About-us/")
def about():
    return render_template("about.html")

@app.route("/Our-impact/")
def impact():
    return render_template("impact.html")

@app.route("/Contact-us/")
def contact():
    return render_template("contact.html")

@app.route("/careers/")
def vacancy():
    return render_template("vacancy.html")

if __name__ == ("__main__"):
    app.run(debug=True)