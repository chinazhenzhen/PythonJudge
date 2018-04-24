from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from flask_login import UserMixin,login_user

from app.models import db
from app import login_manager

class User(db.Model,UserMixin):
    __tablename__="user"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(64))
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



#回掉函数
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  #回掉函数，默认添加