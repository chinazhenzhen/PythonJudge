from flask import jsonify,request,render_template,flash,redirect,url_for
from flask_login import login_required,current_user,login_user,logout_user

from . import web
from app.forms.user import LoginForm,RegisterForm,EditUserInformation
from app.models.user import User,UserInformation

@web.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    next = request.args.get('next')
    if form.validate_on_submit():
        user=User.query_one_user(form.name.data)
        if user is not None and user.confirm_password(form.password.data):
            login_user(user,True) #flask内置函数
            flash("登录成功")
            return redirect(next or url_for('web.index'))
        else:
            flash("登录失败")

    return render_template('user/login.html',form=form)

@web.route("/logout")
def logout():
    logout_user()
    return redirect('/')

@web.route("/register",methods=['GET','POST'])
def register():
    form = RegisterForm()
    use = User()

    if form.validate_on_submit():
        if use.query_one_user(form.name.data) is not None:
            flash("用户名已经存在")
        else:
            use.register_user(form.data)
            flash("success")
            return redirect('/login')

    return render_template('user/register.html',form=form)


@web.route('/userhome/<username>')
def show_user(username):
    db_to_id = User()
    db = UserInformation()
    id = db_to_id.query_one_user(username).id

    return render_template('user/show-user-information.html',user_information = db.query_userinformation(id),user=db_to_id.query_one_user(username),username=username)

@web.route("/edituser",methods=['GET','POST'])
@login_required
def edit_user():
    form = EditUserInformation()
    userinformation_db = UserInformation()

    if form.validate_on_submit():
        userinformation_db.edit_user(current_user.id,form.data)
        flash("更新成功")
        return redirect('/')

    return render_template('user/edit-user-information.html',form=form)




@web.route("/usertest")
@login_required
def testf():
    pass

