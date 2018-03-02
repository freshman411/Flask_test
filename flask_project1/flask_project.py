#-*-coding:utf-8-*-
from flask import Flask,render_template,url_for,request,redirect,flash,session
import config
from db_tables import db
from models import *

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)



##登录验证装饰器
from functools import wraps
def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get('user_id'):   #验证session
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return decorated_function


#主页视图函数
@app.route('/')
def index():
    result = Article.query.all()    # Article.query.order_by('create_time').all() 为排序，反序为order_by('-create_time')

    return render_template('index.html',result=result)

#登录视图函数
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:

        uname = request.form.get('username')
        pwd = request.form.get('password')
        res = User.query.filter(User.username == uname).first()
        if res:
            if res.password == pwd:
                session['user_id'] = res.id         #设置session
                return redirect(url_for('index')) 
            else:
                return '用户名密码错误'
        else:
            return "用户不存在，请先注册"

####注册功能视图函数
@app.route('/register/',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        phone = request.form.get('phone')
        uname = request.form.get('username')
        pwd = request.form.get('password')
        pwd1 = request.form.get('password1')

        user = User.query.filter(User.phone == phone).first()

        if user is not None:
            return "用户已经存在"
        else:
            if phone == "" or uname == "":
                flash('手机号或者用户名不能为空')
                return redirect(url_for('register'))

            elif pwd != pwd1:
                flash('两次输入的密码不匹配')
                return redirect(url_for('register'))
            else:
                user = User(phone=phone,username=uname,password=pwd)
                db.session.add(user)
                db.session.commit()
                # user = User.query.filter(User.phone == phone).first()
                # print (user)
                return redirect(url_for('login'))

##问答视图函数
@app.route('/question/',methods=['GET','POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('requestion.html')

    else:
        title = request.form.get('title')
        content = request.form.get('content')
        article = Article(title=title,content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id==user_id).first()
        article.author = user
        db.session.add(article)
        db.session.commit()
        return  redirect(url_for('index'))

#详情页视图函数
@app.route('/content/<article_id>')
def content(article_id):

    res = Article.query.filter(Article.id==article_id).first()
    count = len(res.answer)
    return render_template('content.html',res=res,count=count)


#问答评论视图函数
@app.route('/answer/',methods=['POST'])
@login_required
def answer():
    answer_content = request.form.get('answer')
    article_id = request.form.get('article-id')

    answer = Anwser(content=answer_content)
    user_id = session['user_id']
    user = User.query.filter(User.id==user_id).first()
    answer.author = user
    article = Article.query.filter(Article.id==article_id).first()
    answer.article = article

    db.session.add(answer)
    db.session.commit()
    return redirect(url_for('content',article_id=article_id))

if __name__ == '__main__':
    app.run()
