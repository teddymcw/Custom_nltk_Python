#using WTF-0.9.3
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Length

class BigText(Form):
	play = TextField('text1', validators=[DataRequired(), Length(min=10, max=25, message="name must be between 10 and 500 characters")])
