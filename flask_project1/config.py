#!/usr/bin/env python
#-*-coding:utf-8-*-

import os

DEBUG=True
SECRET_KEY = os.urandom(24)             #配置session

#dialect+driver://<username>:<password>@<host>:<port>/<dbname>[?<options>]

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'flask'
PASSWORD = 'flask'
HOST = '10.10.10.11'
PORT = '3306'
DATABASE = 'flask_project'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False