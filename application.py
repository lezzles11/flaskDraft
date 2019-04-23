import os
from flask import Flask, render_template, request, flash, redirect, url_for
from app import app
from flask_bootstrap import Bootstrap
from flaskext.sass import sass
from flask_mail import Mail, Message
from flask_wtf import Form, FlaskForm
from wtforms import TextField
from forms import ContactForm

app = Flask(__name__, template_folder='templates', instance_relative_config=True)
app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskDraft.sqlite'),
    )
bootstrap = Bootstrap(app)
sass(app, input_dir='assets/scss', output_dir='static/css')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lesley.yc@gmail.com'
app.config['MAIL_PASSWORD'] = 'Retire69!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def more():
	return render_template("home.html", title = "hello")

@app.route("/weekone")
def thebeginning():
	return render_template("thebeginning.html", title = "Week One")

@app.route("/weektwo")
def weektwo():
	return render_template("weektwo.html", title = "Week Two")

@app.route("/weekthree")
def weekthree():
	return render_template("weekthree.html", title = "Week Three")

@app.route("/weekfour")
def weekfour():
	return render_template("weekfour.html", title = "Week Four")

@app.route("/reflections")
def reflections():
	return render_template("reflections.html", title = "Reflections")

@app.route("/goals")
def goals():
	return render_template("goals.html", title = "Goals")

@app.route("/index")
def index():
	return render_template("index.html", title = "d")

@app.route("/philmed")
def philmed():
	return render_template("philmed.html", title = "Philosophical Meditation")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False: 
			flash('You must enter something into all of the fields')
			return render_template('contact.html', form = form)
		else:
			msg = Message('Hello', sender = 'lesley.yc@gmail.com', recipients = ['lesleyc@bu.edu'])
			msg.body = """
			From: %s %s <%s>
			%s
			""" % (form.firstName.data, form.lastName.data, form.email.data, form.message.data)
			mail.send(msg)
			return render_template('contact.html', success=True)
	elif request.method == 'GET':
		return render_template('contact.html',
			title = 'Contact Us',
			form = form)
	

@app.errorhandler(404)
def page_not_found(error):
	return render_template("404.html", title = "404"), 404




if __name__ == '__main__':
   app.run(debug = True)



