from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flaskext.sass import sass
import flask_login
import config
import os 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.config['SECRET_KEY'] = 'you-will-never-guess'
db = SQLAlchemy(app)
"""
app.secret_key = 'super secret string'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
users = {'foo@bar.tld': {'password': 'secret'}}
"""
bootstrap = Bootstrap(app)

sass(app, input_dir='assets/scss', output_dir='static/css')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')



@app.route('/login')
def login():
    form = LoginForm()
    return render_template('templates/authlogin.html', title='Sign In', form=form)



@app.route("/")
def index():
    return render_template("more.html")

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



"""
class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'



"""


if __name__ == '__main__':
    app.run(debug=True)


