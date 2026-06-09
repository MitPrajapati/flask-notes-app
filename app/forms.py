from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length

class registerForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(message='username should be required'),Length(min=3,max=20)])
    email = StringField('email',validators=[DataRequired(message='Email Must be required')])
    password = PasswordField('password',validators=[DataRequired(message='Password should be required'),Length(min=6,message = 'password should be 6 character long')])
class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(message='username should be required'),Length(min=3,max=20)])
    password = PasswordField('password',validators=[DataRequired(message='Password should be required'),Length(min=6,message = 'password should be 6 character long')])