from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_migrate import Migrate, MigrateCommand
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_script import Manager

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
	'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Post(db.Model):
	__tablename__ = 'post'
	id = db.Column(db.Integer(), primary_key=True)
	title = db.Column(db.String(80), unique=True)
	post_text = db.Column(db.String(255))

	def __init__(self, title, post_text):
		self.title = title
		self.post_text = post_text

class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	post_text = StringField('Post_Text',                            
							 validators=[DataRequired()]
						   )
