import os
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flaskext.sass import sass
from flask_mail import Mail, Message
from flask_wtf import Form
from wtforms import TextField
from forms import ContactForm, RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy 
from flask_marshmallow import Marshmallow 
import datetime
from marshmallow import Schema, fields, pre_load, validate

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

db = SQLAlchemy(app)
#start the marshmallow
#marshmallow helps you convert more complicated objects 
ma = Marshmallow(app) 
bootstrap = Bootstrap(app)

#initializing the database 
class philMed(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	anxious = db.Column(db.Text, nullable=False)
	upset = db.Column(db.Text, nullable=False)
	excited = db.Column(db.Text, nullable=False)

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
@app.route("/philMed", methods=['POST'])
def add_philMed():
	form = philMedForm()
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
