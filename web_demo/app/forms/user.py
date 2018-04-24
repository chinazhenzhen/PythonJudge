from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,IntegerField,PasswordField
from wtforms.validators import Length,DataRequired

class LoginForm(FlaskForm):
    name=StringField("帐号",validators=[DataRequired(),Length(min=1,max=30)])
    password=PasswordField("密码",validators=[DataRequired(),Length(min=1,max=30)])
    login=SubmitField("登录")

class RegisterForm(FlaskForm):
    name = StringField("帐号", validators=[DataRequired(), Length(min=1, max=30)])
    password = PasswordField("密码", validators=[DataRequired(), Length(min=1, max=30)])
    login = SubmitField("注册")