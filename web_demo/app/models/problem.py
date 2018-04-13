from sqlalchemy import Column,Integer,String,DateTime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

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


class problem_status(db.Model):
    run_id = Column(Integer,primary_key=True,autoincrement=True)
    problem_id = Column(Integer)
    result = Column(Integer,default=1)
    remember = Column(Integer,default=0)
    time = Column(Integer,default=0)
    language = Column(Integer,default=1)
    code = Column(String(20000))
    code_len = Column(Integer)
    #submit_time = Column(DateTime,nullable=False)

    def __repr__(self):
        return '<run_id %r>' % self.run_id




class Test(db.Model):

    testname = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)