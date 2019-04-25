from manage import db,app
from datetime import datetime 

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True, nullable=False)
	email = db.Column(db.String(120), index=True, unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False)
	password = db.Column(db.String(60), nullable=False)
	#User has relationship with post model 
	posts = db.relationship('Post', backref='author', lazy=True)
	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')" 

class Post(db.Model):
	id = db.Column(dbInteger, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id', nullable=False))
	def __repr__(self):
		return f"User('{self.title}', '{self.date_posted}')" 