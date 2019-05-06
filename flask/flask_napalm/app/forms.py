from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, IPAddress

class LoginForm(FlaskForm):
    ''' A simple class to get username, password and IP or MAC address '''
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    ipaddress = StringField('IP Address', validators=[IPAddress()])
    submit = SubmitField('Enter')
