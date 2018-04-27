from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
import datetime

from app.models import db

status = {
    1:"running",
    2:"accepted",
    3:"wrong"
}

yuyan = {
    1:"no language",
    2:"C",
    3:"C++"
}

class problem(db.Model):
    __tablename__ = "problem"

    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),unique=True,nullable=False)
    description = Column(String(2000))
    input_description = Column(String(2000))
    output_description = Column(String(2000))
    input_example = Column(String(1000))
    output_example = Column(String(1000))
    hint = Column(String(1000))
    source = Column(String(1000))
    input_test = Column(String(2000))
    output_test = Column(String(2000))

    def __repr__(self):
        return '<problem-id %r>' % self.id

    def edit_problem(self,data):
        self.title = data.title.data
        self.description = data.description.data
        self.input_description = data.input_description.data
        self.output_description = data.output_description.data
        self.input_example = data.input_example.data
        self.output_example = data.output_example.data
        self.hint = data.hint.data
        self.source = data.source.data
        self.input_test = data.input_test.data
        self.db_t.output_test = data.output_test.data

        db.session.add(self)

    @staticmethod
    def query_problem():
        data = problem.query.all()
        return data

    @staticmethod
    def query_one_problem(problem_id):
        data = problem.query.filter_by(id=problem_id).first()
        return data


class problem_status(db.Model):
    __tablename__ = "problem_status"

    run_id = Column(Integer,primary_key=True,autoincrement=True)
    ##problem.id作为problem_status的外建
    problem_id = Column(Integer,ForeignKey('problem.id'))
    #通过problem_info就可以查询相关信息
    problem_infor = db.relationship('problem',backref=db.backref('problem_status'))
    user_name = Column(String(64))
    result = Column(Integer,default=1)
    remember = Column(Integer,default=0)
    time = Column(String(32))
    language = Column(Integer,default=1)
    code = Column(String(20000))
    code_len = Column(Integer)
    #submit_time = Column(DateTime,nullable=False)

    def __repr__(self):
        return '<run_id %r>' % self.run_id

    def submit_code(self,data):
        self.problem_id = data['id']
        self.language = data['language']
        self.code = data['code']
        self.user_name = data['user_name']
        now = datetime.datetime.now()
        self.time = now.strftime('%Y-%m-%d %H:%M:%S') #获得时间戳，最好写成函数

        db.session.add(self)

    @staticmethod
    def query_db_status():
        status_data = problem_status.query.order_by(problem_status.run_id.desc()).all()
        db.session.rollback()
        return status_data


class Test(db.Model):

    testname = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)