#!/usr/bin/env python
#-*-coding:utf-8-*-

##创建数据库表信息

from db_tables import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    phone = db.Column(db.String(11),nullable=False)
    username = db.Column(db.String(32),nullable=False)
    password = db.Column(db.String(32),nullable=False)


class Article(db.Model):
    __tablename = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30),nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now())
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    author = db.relationship('User',backref=db.backref('questions'))


class Anwser(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    article_id = db.Column(db.Integer,db.ForeignKey(Article.id))
    author_id = db.Column(db.Integer,db.ForeignKey(User.id))
    create_date = db.Column(db.DateTime,default=datetime.now())

    #表示将article字段属性映射到Article模型（表），通过Answer.article可查看Article表的内容，同样可通过Article.answer（backref设置的）查看Answer表的内容
    article = db.relationship('Article',backref=db.backref('answer',order_by=create_date.desc()))   #查询时排序
    #表示将author字段属性映射到User模型（表），通过Answer.author可查看User表的内容，同样可通过User.answer（backref设置的）查看Answer表的内容
    author  = db.relationship('User',backref=db.backref('answer'))
    

