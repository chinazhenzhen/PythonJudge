from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,JSON
from flask_login import UserMixin,login_user

from app.models import db
from app import login_manager

class User(db.Model,UserMixin):
    __tablename__="user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(64),unique=True)
    password = Column(String(64))

    @staticmethod
    def query_one_user(name):
        data = User.query.filter_by(name=name).first()
        return data

    def register_user(self,data):
        self.name = data['name']
        self.password = data['password']

        db.session.add(self)

    def confirm_password(self,password):
        if self.password == password:
            return True
        return False

class UserInformation(db.Model):
    '''
    配合user使用
    '''
    __tablename__ = "userinformation"
    id = Column(Integer,primary_key=True)
    real_name = Column(String(64))
    hduoj_name = Column(String(64))
    coderforces_name = Column(String(64))
    accepted_number = Column(Integer,default=0)
    submission_number = Column(Integer,default=0)
    problem_status = Column(JSON,default={})
    phone_number = Column(String(15))
    school = Column(String(200))
    student_id = Column(String(24))



#回掉函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  #回掉函数，默认添加