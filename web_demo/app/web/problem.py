from flask import jsonify,request,render_template,flash,redirect
from flask_login import current_user

from . import web
from app.forms.problem import edit_problem_form,edit_code_form
from app.models.problem import problem,problem_status
#from app.db_save.problem import problem_db,problem_db_status

@web.route('/')
def index():
    return render_template('index.html')


@web.route('/editproblem',methods=['GET','POST'])
def edit_problem():
    db = problem()
    form = edit_problem_form()
    if form.validate_on_submit():
        db.edit_problem(form)

    return render_template('edit-problem.html',form=form)


@web.route('/showproblem')
def show_problem():
    db = problem()
    
    return render_template('show-problem.html',data=db.query_problem())

@web.route('/showstatus')
def show_status():
    db_code = problem_status()

    return render_template('show-problem-status.html',data=db_code.query_db_status())


@web.route('/showproblem/<id>',methods=['GET','POST'])
def show_one_problem(id):
    db = problem()
    db_code = problem_status()
    form = edit_code_form()
    
    if form.validate_on_submit():
        data={}
        data['id'] = id
        data['code'] = form.code.data
        data['language'] = form.code_language.data
        data['user_name'] = current_user.name
        db_code.submit_code(data)
        return redirect("/showstatus")
    else:
        return render_template('show-one-problem.html',p_one=db.query_one_problem(id),form=form)


@web.route('/test')
def test():
    return "hello"