from flask import jsonify,request,render_template,flash,redirect


from . import web
from app.forms.problem import ProblemForm
from app.db_save.problem import ProblemDb

@web.route('/',methods=['GET','POST'])
def editproblem():
    form = ProblemForm()
    db = ProblemDb()
    if form.validate_on_submit():
        db.saveinformation(form)
    return render_template('problem.html',form=form)

@web.route('/showproblem')
def showproblem():
    pass

@web.route('/test')
def test():
    return "hello"