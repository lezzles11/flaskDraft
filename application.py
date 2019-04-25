import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flaskext.sass import sass
from flask_mail import Mail, Message
from flask_wtf import Form
from wtforms import TextField
from forms import ContactForm, RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
from database import db_session
import models

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app = Flask(__name__, instance_relative_config=True)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
sass(app, input_dir='assets/scss', output_dir='static/css')


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    category = db.relationship('Category',
        backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lesley.yc@gmail.com'
app.config['MAIL_PASSWORD'] = 'Retire69!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/delete/')
def delete():
    u = User.query.get(i)
    db.session.delete(u)
    db.session.commit()
    return "user deleted"

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

@app.route("/contact1")
def contact1():
	return render_template("contact1.html", title = "contact1")

@app.route("/draft")
def draft():
	return render_template("draft.html", title = "draft")

@app.route("/process")
def process():
	return render_template("process.html", title = "process")

@app.route("/store")
def store():
	return render_template("store.html", title = "store")

@app.route("/testing_home")
def testing_home():
	return render_template("testing_home.html", title = "testing_home")


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
	
"""
@app.errorhandler(404)
def page_not_found(error):
	return render_template("404.html", title = "404"), 404
"""



if __name__ == '__main__':
   app.run(debug = True)



