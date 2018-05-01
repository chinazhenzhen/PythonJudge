from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
import datetime

from app.models import db
from app.setting import JudgeConfig


class problem(db.Model):
    __tablename__ = "problem"

    #题目id
    id = Column(Integer,primary_key=True,autoincrement=True)
    #题目标题
    title = Column(String(50),unique=True,nullable=False)
    #时间限制
    time_limit = Column(Integer,nullable=True)
    #空间限制
    memory_limit = Column(Integer,nullable=True)
    #题目描述
    description = Column(String(2000))
    #输入描述
    input_description = Column(String(2000))
    #输出描述
    output_description = Column(String(2000))
    #输入样例
    input_example = Column(String(1000))
    #输出样例
    output_example = Column(String(1000))
    #题目提示
    hint = Column(String(1000))
    #题目来源/出题人
    source = Column(String(1000))
    #输入测试数据
    input_test = Column(String(2000))
    #输出测试数据
    output_test = Column(String(2000))
    #总共提交的数目
    total_submission_number = Column(Integer,default=0)
    #总共AC的题目数
    total_accepted_number = Column(Integer,default=0)

    #外建关系，问题和该问题的提交是一对多的关系
    problem_statuses = db.relationship('problem_status') #建立关系

    def __repr__(self):
        return '<problem-id %r>' % self.id

    def edit_problem(self,data):
        self.title = data.title.data
        self.time_limit = data.time_limit.data
        self.memory_limit = data.memory_limit.data
        self.description = data.description.data
        self.input_description = data.input_description.data
        self.output_description = data.output_description.data
        self.input_example = data.input_example.data
        self.output_example = data.output_example.data
        self.hint = data.hint.data
        self.source = data.source.data
        self.input_test = data.input_test.data
        self.output_test = data.output_test.data

        db.session.add(self)

    @staticmethod
    def query_problem():
        data = problem.query.all()
        return data

    @staticmethod
    def query_one_problem(problem_id):
        data = problem.query.filter_by(id=problem_id).first()
        return data

    @staticmethod
    def query_one_problem_status(problem_id):
        '''
        :return: 一个问题的所有提交记录
        '''
        data = problem_status.query.filter_by(problem_id=problem_id).order_by(problem_status.run_id.desc()).all()
        return data



class problem_status(db.Model):
    __tablename__ = "problem_status"

    run_id = Column(Integer,primary_key=True,autoincrement=True)
    ##problem.id作为problem_status的外建
    problem_id = Column(Integer,ForeignKey('problem.id')) #外键
    #通过problem_info就可以查询相关信息
    problem_infor = db.relationship('problem')  #建立关系
    #提交人
    user_name = Column(String(64))
    #提交结果
    result = Column(Integer,default=JudgeConfig.result_id["pending"])
    #内存
    memory = Column(Integer,default=0)
    #运行时间
    runtime = Column(Integer,default=0)
    #提交时间
    time = Column(String(32))
    #语言
    language = Column(Integer,default=1)
    #代码
    code = Column(String(20000))
    #代码长度
    code_len = Column(Integer)
    #err错误信息
    error = Column(String(1024))



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

    def add_problem_submission(self):
        the_problem = problem.query().filter_by(id=self.problem_id).first()
        the_problem.total_submission_number = int(the_problem.total_submission_number)+1

    #judge后进行提交
    @staticmethod
    def add_problem_accepted(is_ac,data):
        the_problem = problem.query().filter_by(id=data["problem_id"]).first()
        the_problem_status = problem_status.query().filter_by(run_id=data["run_id"]).first()
        if (is_ac):
            the_problem.total_accepted_number = int(the_problem.total_accepted_number) + 1
        the_problem_status.time = data["time"]
        the_problem_status.memory = data["memory"]
        the_problem_status.result = data["result"]
        the_problem_status.error = data["error"]


class Test(db.Model):

    testname = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)