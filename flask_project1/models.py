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

    article = db.relationship('Article',backref=db.backref('answer',order_by=create_date.desc()))
    author  = db.relationship('User',backref=db.backref('answer'))

