from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


@app.route("/campus-tour", methods=["GET"])
def campus_tour():
    return render_template("campus_tour.html")

app.run(debug=True)