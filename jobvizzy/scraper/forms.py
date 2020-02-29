from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class JobCityForm(FlaskForm):
  pass
  jobTitle = StringField('Title', validators=[DataRequired()],default='Developer')
  cityName = StringField('Title', validators=[DataRequired()],default='Denver')
 
