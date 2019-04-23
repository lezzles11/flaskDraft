import os
"""
app.config['SECRET_KEY'] = 'you-will-never-guess'
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
"""


MAIL_FROM_EMAIL = "lesley.yc@gmail.com" # For use in application emails
SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'
SQLALCHEMY_DATABASE_URI = "postgresql://user:password@localhost/spaceshipDB"
