from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/thebeginning")
def thebeginning():
    return render_template("thebeginning.html")

@app.route("/reflections")
def reflections():
    return render_template("reflections.html")





