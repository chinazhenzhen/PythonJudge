from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,SelectField,TextAreaField
from wtforms.validators import Length,DataRequired,Required

class edit_problem_form(FlaskForm):
    title = StringField(validators=[DataRequired(),Length(min=1,max=30)])
    description = TextAreaField(validators=[DataRequired(),Length(min=1,max=100000)])
    time_limit = IntegerField(validators=[DataRequired()])
    memory_limit = IntegerField(validators=[DataRequired()])
    input_description = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    output_description = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    input_example = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    output_example = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    hint = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    source = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    input_test = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    output_test = StringField(validators=[DataRequired(),Length(min=1,max=1000)])
    submit = SubmitField("提交")

#RadioField('method', choices=[(1,'GET'),(2,'POST')],default=1)
class edit_code_form(FlaskForm):
    #code_language = IntegerField(validators=[DataRequired()])
    code_language = SelectField("选择语言",validators=[DataRequired()],choices=[('1','C++'),('2','C')])
    code = TextAreaField("编写代码",validators=[DataRequired()])
    submit = SubmitField("提交代码")