from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

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

@app.route("/goals")
def goals():
    return render_template("goals.html")

@app.route("/testing")
def testing():
    return render_template("testing.html")

if __name__ == '__main__':
    app.run(debug=True)





