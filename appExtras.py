import os
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from flask_wtf import Form
from wtforms import TextField
from forms import ContactForm, RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy 
from flask_marshmallow import Marshmallow 
import datetime
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

#app core 
app = Flask(__name__, instance_relative_config=True)
#locating Database
basedir = os.path.abspath(os.path.dirname(__file__))
#converting scss to css 
#now, actually MAKING database
#looking for a file called db.sqlite in the current folder structure 
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://localhost/practicedb'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)
#stopping it from complaining 
#Initialize the databse (or, start the database)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
#start the marshmallow
#marshmallow helps you convert more complicated objects 
ma = Marshmallow(app) 
bootstrap = Bootstrap(app)
class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), unique=True)
    post_text = db.Column(db.String(255))

    def __init__(self, title, post_text):
        self.title = title
        self.post_text = post_text
"""
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

@app.route("/practiceForm", methods=["POST", "GET"])
def practiceForm():
    if request.method == "POST":
        username = request.form['username']        
        age = request.form['age']        
        email = request.form['email']        
        hobbies = request.form['hobbies']        
        return redirect(url_for("practiceData",                              
                                username=username,
                                age=age,
                                email=email,   
                                hobbies=hobbies))  
    return render_template("practiceForm.html", title = "Practice Form")

@app.route("/practiceData", methods=["GET"])
def practiceData():
    username = request.args.get('username')    
    age = request.args.get('age')    
    email = request.args.get('email')    
    hobbies = request.args.get('hobbies')    
    return render_template("practiceData.html",
                           username=username,                         
                           age=age,                          
                           email=email,                         
                           hobbies=hobbies
                           )
    


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



