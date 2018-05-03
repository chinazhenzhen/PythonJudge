from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,IntegerField,PasswordField
from wtforms.validators import Length,DataRequired,Email,IPAddress

class LoginForm(FlaskForm):
    name=StringField("帐号",validators=[DataRequired(),Length(min=1,max=30)])
    password=PasswordField("密码",validators=[DataRequired(),Length(min=1,max=30)])
    login=SubmitField("登录")

class RegisterForm(FlaskForm):
    name = StringField("帐号", validators=[DataRequired(), Length(min=1, max=30)])
    password = PasswordField("密码", validators=[DataRequired(), Length(min=1, max=30)])
    login = SubmitField("注册")

class EditUserInformation(FlaskForm):
    real_name = StringField("真实姓名",validators=[DataRequired(),Length(min=0,max=30)])
    #avatar = StringField("真实姓名",validators=[DataRequired(),Length(min=0,max=30)])
    mood = StringField("个性签名",validators=[DataRequired(),Length(min=0,max=300)])
    email = StringField("电子邮箱",validators=[DataRequired(),Length(min=0,max=300),Email()])
    blog_address = StringField("博客地址",validators=[DataRequired(),Length(min=0,max=300)])
    github = StringField("Github",validators=[DataRequired(),Length(min=0,max=300)])
    hduoj_name = StringField("hdu昵称",validators=[DataRequired(),Length(min=0,max=64)])
    coderforces_name = StringField("coderforces昵称",validators=[DataRequired(),Length(min=0,max=64)])
    phone_number = StringField("手机号码",validators=[DataRequired(),Length(min=0,max=15)])
    school = StringField("学校",validators=[DataRequired(),Length(min=0,max=128)])
    student_id = StringField("学生学号",validators=[DataRequired(),Length(min=0,max=20)])

    update = SubmitField("提交")