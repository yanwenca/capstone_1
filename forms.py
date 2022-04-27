from wtforms import SelectField, StringField, FloatField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class SurveyForm(FlaskForm):

    q1 = StringField("q1", validators=[InputRequired()])
    q2 = StringField("q2", validators=[InputRequired()])
    q3 = FloatField("q3", validators=[InputRequired()])
    q4 = StringField("q4", validators=[InputRequired()])
    q5 = StringField("q5", validators=[InputRequired()])

