from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])