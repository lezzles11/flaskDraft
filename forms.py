from flask_wtf import Form, FlaskForm
from wtforms import TextField, IntegerField, StringField, SelectField, DateField, TextAreaField, SubmitField, BooleanField, validators, PasswordField
from wtforms.validators import Required, DataRequired, ValidationError, Length, Email, EqualTo

class philmed(Form):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
   Address = TextAreaField("Address")
   
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'), 
      ('py', 'Python')])
   submit = SubmitField("Send")

class ContactForm(Form):
   firstName = TextField('First Name', [validators.DataRequired("Enter your first name")])
   lastName = TextField('Last Name', [validators.DataRequired("Enter your last name")])
   email = TextField('E-mail', [validators.DataRequired("Enter a valid email address"), validators.Email("Enter a valid email address")])
   subject = TextField('Subject', [validators.DataRequired("What's the nature of your message?")])
   message = TextAreaField('Message', [validators.DataRequired("Didn't you want to say something?")])
   submit = SubmitField('Send')


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')