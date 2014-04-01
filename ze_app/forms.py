#using WTF-0.9.3
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Length

class BigText(Form):
	play = TextField(u'text1', validators=[DataRequired(), Length(min=10, 
		max=50000, message="name must be between 10 and 50000 characters")])

class SingleWord(Form):
	single_word = TextField(u'single-word', validators=[DataRequired(), Length(min=2, 
		max=80, message="name must be between 2 and 80 characters")])

