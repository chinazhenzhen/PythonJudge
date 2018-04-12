from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Length,DataRequired

class ProblemForm(FlaskForm):
    title = StringField(validators=[DataRequired(),Length(min=1,max=30)])
    description = TextAreaField()
    input_description = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    output_description = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    input_example = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    output_example = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    hint = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    source = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    input_test = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    output_test = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    submit = SubmitField("提交")