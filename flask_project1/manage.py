#!/usr/bin/env python
#-*-coding:utf-8-*-

#程序入口

from flask_script import  Manager
from flask_migrate import Migrate,MigrateCommand
from flask_project import app
from db_tables import db
from models import *


manager = Manager(app)                       #初始化应用
migrate = Migrate(app,db)                   #使用migrate绑定app和db
manager.add_command('db',MigrateCommand)         #添加迁移脚本命令到manager中

# db.create_all()


if __name__ == '__main__':
    manager.run()