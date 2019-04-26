import os
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flaskext.sass import sass
from flask_mail import Mail, Message
from flask_wtf import Form
from wtforms import TextField
from forms import ContactForm
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy 
from flask_marshmallow import Marshmallow 
import datetime
from marshmallow import Schema, fields, pre_load, validate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

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

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
WTF_CSRF_SECRET_KEY = SECRET_KEY

db = SQLAlchemy(app)
#start the marshmallow
#marshmallow helps you convert more complicated objects 
ma = Marshmallow(app) 
bootstrap = Bootstrap(app)


#initializing the database 
class philMed(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), nullable=False)
	date_posted = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	anxious = db.Column(db.String(200), nullable=False)
	upset = db.Column(db.String(200), nullable=False)
	excited = db.Column(db.String(200), nullable=False)

	def __init__(self, title, date_posted, anxious, upset, excited):
		#when these are passed in, you want to add them to the instance 
		self.title = title
		self.date_posted = date_posted
		self.anxious = anxious
		self.upset = upset
		self.excited = excited 


#Marshmallow part 
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

#POST -> send or whatever. 



def save_changes(philMed, form, new=False):

	#render_template('philMed.html', form=form)
	#flash('Try again')
	if new:
		title = request.json['title']
		anxious = request.json['anxious']
		upset = request.json['upset']
		excited = request.json['excited']
		new_philMed = philMed(title, anxious, upset, excited)
	#add the data 
		db.session.add(new_philMed)
		db_session.commit() 
		return philMed_schema.jsonify(new_philMed)
	return render_template('philMed.html', form=form)


@app.route("/philMed", methods=['POST'])
def add_philMed():
	form = render_template('philMed.html', form=form)
	if form.validate():
		philMed = PhilMed()
		save_changes(philMed, form, new=True)
		flash('Yay!')
		return redirect('/')
	return render_template('philMed.html', form=form)


"""
def save_changes(philMed, form, new=False):
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
	if new==False:

return render_template('philMed.html', form=form)

def save_changes(philMed, form, new=False):
	philMed.title = form.title.data
	philMed.anxious = form.anxious.data
	philMed.upset = form.upset.data
	philMed.excited = form.excited.data
	if new:
		db_session.add(philMed)
	db_session.commit() 


@app.route('/philMed', methods=['POST'])
def data_philMed():
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
return render_template('philMed.html', form=form)
"""
#GETTING ALL YOUR POSTS

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search.data['search'] == '':
        qry = philMed.query.all()
        results = philMed_schema.dump(all_philMeds)
 
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = philMed(results)
        table.border = True
        return render_template('dataphilmed.html', table=table)


@app.route('/philMed', methods=['GET'])
def get_philMeds():
	results = []
	if search.data 
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


mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lesley.yc@gmail.com'
app.config['MAIL_PASSWORD'] = 'Retire69!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


#DELETING 
@app.route("/philMed/<id>", methods=['DELETE'])
def delete_philMed(id):
	philMed = philMed.query.get(id)
	db.session.delete(philMed)
	db.session.commit()
	
	return philMed_schema.jsonify(philMed)


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



	

#run server 
if __name__ == '__main__':
   app.run(debug = True)


