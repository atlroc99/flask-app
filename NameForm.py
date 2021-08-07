from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('Enter your email address: ', [validators.DataRequired(), validators.Email()])
    gender = StringField('Enter Gender', validators=[DataRequired()])
    submit = SubmitField('Submit')
