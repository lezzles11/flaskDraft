from application import db
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from database import Base, metadata, db_session

#self = 
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

"""
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

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


class User(object):
    query = db_session.query_property()

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), unique=True),
    Column('email', String(120), unique=True)
)
mapper(User, users)

"""