from flask import Flask
from app.models.problem import db
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
#from flask_migrate import Migrate,MigrateCommand
#from flask_script import Manager

bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'web.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')  # 核心对象导入配置文件
    app.config.from_object('app.setting')  # 核心对象导入配置文件
    register_blueprint(app)  # 蓝图注册

    db.init_app(app)
    db.create_all(app=app)  #创建数据库

    #migrate = Migrate(app,db)
    #manager = Manager(app)
    #manager.add_command('db',MigrateCommand)

    bootstrap.init_app(app)  #加载bootstrap模块

    login_manager.init_app(app)  #加载登录验证模块



    return app

#蓝图注册函数
def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)