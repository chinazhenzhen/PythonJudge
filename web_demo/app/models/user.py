from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,JSON
from flask_login import UserMixin,login_user
import datetime

from app.models import db
from app import login_manager

USER = 0
ADMIN = 1
SUPER_ADMIN = 2

class User(db.Model,UserMixin):
    __tablename__="user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    #账户名
    name = Column(String(64),unique=True)
    #密码
    password = Column(String(64))
    #账号创建时间
    create_time = Column(String(64))
    #用户权限
    admin_type = Column(Integer,default=USER)

    @staticmethod
    def query_one_user(name):
        data = User.query.filter_by(name=name).first()
        return data

    def register_user(self,data):
        self.name = data['name']
        self.password = data['password']
        now = datetime.datetime.now() #创建时间
        self.create_time = now.strftime('%Y-%m-%d %H:%M:%S')  # 获得时间戳，最好写成函数

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
    #真实姓名
    real_name = Column(String(64))
    #头像，储存地址
    avatar = Column(String(128))
    #个性签名
    mood= Column(String(200))
    #博客地址
    blog_address = Column(String(200))
    #hdu昵称
    hduoj_name = Column(String(64))
    #cf昵称
    coderforces_name = Column(String(64))
    #ac数
    accepted_number = Column(Integer,default=0)
    #提交数
    submission_number = Column(Integer,default=0)
    #手机号
    phone_number = Column(String(15))
    #学校
    school = Column(String(200))
    #学号
    student_id = Column(String(24))
    #AC题号统计
    problem_status = Column(JSON, default={})

    def edit_user(self,data):
        self.real_name = data['real_name']
        self.avatar = data['avatar']
        self.mood = data['mood']
        self.blog_address = data['blog_address']
        self.hduoj_name = data['hduoj_name']
        self.coderforces_name = data['coderforces_name']
        self.phone_number = data['phone_number']
        self.school = data['school']
        self.student_id = data['student_id']

        db.session.add(self)



#回掉函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  #回掉函数，默认添加