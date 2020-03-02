from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class JobForm(FlaskForm):
  pass
  jobTitle = StringField('Title', validators=[DataRequired()],default='Developer')
 

class CityForm(FlaskForm):
  pass
  cityName = StringField('Title', validators=[DataRequired()],default='Denver')
 

class JobCityPairForm(FlaskForm):
  pass

  jobTitle = StringField('JobTitle', validators=[
                         DataRequired()], default='Developer')
  city = StringField('City', validators=[
                         DataRequired()], default='Denver')


