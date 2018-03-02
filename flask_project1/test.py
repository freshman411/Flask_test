#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys

login_user = {"is_login":False}

def outer(func):
    def inner(*args,**kwargs):
        if login_user["is_login"]:
            r = func()								###这里将函数的值赋给一个变量，可打印出来
            return r
        else:
            print("please login")
    return inner

@outer
def change_pass():
        print ("welcome back %s,the function is change_pass" % login_user['user'])
        sys.exit()

@outer
def manager():
    print ("welcome back %s,the function is manager" % login_user['user'])
    sys.exit()

def login(uname,pwd):
    if uname == "freshman" and pwd == "freshman":
        login_user["is_login"] = True
        login_user['user'] = uname
        manager()

    else:
        print ("invial username or password,please try again!")

def main():
    while True:
        a = input("1,后台管理;2,登录")
        if a == '1':
            manager()
        elif a == '2':
            uname = input('username:')
            pwd = input('password:')
            login(uname,pwd)

main()