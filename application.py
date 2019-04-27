import os
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flaskext.sass import sass
from flask_mail import Mail, Message
from forms import ContactForm, philMed
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy 
import datetime
from db_setup import init_db, db_session
from table import philMed
from models import philMed
from marshmallow import fields, Schema, validates, ValidationError


#app core 
app = Flask(__name__, instance_relative_config=True)
#locating Database
basedir = os.path.abspath(os.path.dirname(__file__))
#converting scss to css 
sass(app, input_dir='assets/scss', output_dir='static/css')
#now, actually MAKING database
#looking for a file called db.sqlite in the current folder structure 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#stopping it from complaining 
#Initialize the databse (or, start the database)

SECRET_KEY = 'Retire69!'

db = SQLAlchemy(app)
#start the marshmallow
#marshmallow helps you convert more complicated objects 
#ma = Marshmallow(app) 
bootstrap = Bootstrap(app)



#Marshmallow part 
"""
class philMedSchema(ma.Schema):
	class Meta:
		#what you want to show
		fields = ('id', 'title', 'date_posted', 'anxious', 'upset', 'excited')

#RUN from application import db, then db.create_all()
#starting the schema 
#strict = true (prevent the warning)

philMed_schema = philMedSchema(strict=True)

#dealing with more than one
philMeds_schema = philMedSchema(many=True, strict=True)
"""
#POST -> send or whatever. 
@app.route("/philMed", methods=['POST'])
def add_philMed():
	title = request.json['title']
	anxious = request.json['anxious']
	upset = request.json['upset']
	excited = request.json['excited']

	#starting new object here
	new_philMed = philMed(title, anxious, upset, excited)
	#add the data 
	db.session.add(new_philMed)
	#save
	db.session.commit()

	return philMed_schema.jsonify(new_philMed)

#GETTING ALL YOUR POSTS
@app.route('/philMed', methods=['GET'])
def get_philMeds():
	all_philMeds = philMed.query.all()
	result = philMed_schema.dump(all_philMeds)
	return jsonify(result.data)

#GETTING ONE POST 
@app.route('/philMed/<id>', methods=['GET'])
def get_philMed(id):
	philMed = philMed.query.get(id)
	return philMed_schema.jsonify(philMed)

#UPDATING 
@app.route("/philMed/<id>", methods=['PUT'])
def update_philMed(id):
	philMed = philMed.query.get(id)

	title = request.json['title']
	anxious = request.json['anxious']
	upset = request.json['upset']
	excited = request.json['excited']

	#construct new product to submit to database
	philMed.title = title
	philMed.anxious = anxious
	philMed.upset = upset
	philMed.excited = excited

	#save (no need to add)
	db.session.commit()

	return philMed_schema.jsonify(philMed)


#DELETING 
@app.route("/philMed/<id>", methods=['DELETE'])
def delete_philMed(id):
	philMed = philMed.query.get(id)
	db.session.delete(philMed)
	db.session.commit()
	
	return philMed_schema.jsonify(philMed)


"""

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


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
"""

mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lesley.yc@gmail.com'
app.config['MAIL_PASSWORD'] = 'Retire69!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True



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


"""
#POST -> send or whatever. 
@app.route("/philMed", methods=['POST'])
def philMed():
	return render_template("philmed.html", title = "Philosophical Meditation")
"""



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


#run server 
if __name__ == '__main__':
   app.run(debug = True)



