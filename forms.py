from flask_wtf import FlaskForm
from wtforms.fields.core import BooleanField, StringField
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

'''
    crete a registraion from inherited from FlaskForm
    the registraion form will have some fields that will also 
    be imported from the wtfforms - such as StringField, Email, etc
    
    Form Fields Validator: 
    username - StringField : char between 2-20 char, not empty
'''


class RegistrationForm(FlaskForm):
    username = StringField(
        label='Username',
        description='registration username',
        validators=[DataRequired(), Length(min=2, max=10)])

    email = StringField(
        label='Email',
        description='Enter a valid email',
        validators=[DataRequired(), Email()])

    password = PasswordField(
        label='Password',
        description='Enter a proper password',
        validators=[DataRequired()])

    confirm_password = PasswordField(
        label='Confirm Password',
        validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField(label='Register')


class LoginForm(FlaskForm):
    email = StringField(
        label='Email',
        validators=[DataRequired(), Email()]
    )

    passwordd = PasswordField(label='password', validators=[DataRequired()])

    # we need a remember me check box field - true or false
    remember_user = BooleanField(label='Remember me')

    login = SubmitField(label='Login')
