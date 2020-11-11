from flask import Flask,render_template,url_for,request,redirect,session
from flask import send_file
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import image_data
import requests
import crawl

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///databases/user_databases/cnir.db'
app.secret_key="cnirsecretkeyforsession"
db=SQLAlchemy(app)
class search_history(db.Model):
    search_id=db.Column(db.Integer,primary_key=True)
    search_keywords=db.Column(db.String(200),nullable=False,unique=True)
    search_datetime=db.Column(db.DateTime,default=datetime.now)
    user_id=db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return '<search_row %r>' % self.search_id
class user_account(db.Model):
    user_id=db.Column(db.Integer,primary_key=True)
    user_firstname=db.Column(db.String(200),nullable=False)
    user_lastname=db.Column(db.String(200),nullable=False)
    user_email=db.Column(db.String(200),nullable=False,unique=True)
    user_password=db.Column(db.String(200),nullable=False)
    def __repr__(self):
        return '<user_row %r>' % self.user_id
class user_interest(db.Model):
    interest_id=db.Column(db.Integer,primary_key=True)
    interest_name=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,nullable=False)
    def __repr__(self):
        return '<interest_row %r>' % self.interest_id

def past_news():
    keywords=search_history.query.all()
    if keywords:
        for i in keywords:
            print("result for ",i.search_keywords)
            news=i.search_keywords
            print(crawl.crawler(news))
past_news()

try:
    from latest_nation import latest_nation_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    latest_nation_list={}
try:
    from latest_dawn import latest_dawn_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    latest_dawn_list={}
try:
    from latest_pakistan_today import latest_pakToday_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    latest_pakToday_list={}
try:
    from latest_daily_pakistan import latest_dailyPak_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    latest_dailyPak_list={}
try:
    from latest_tribune import latest_tribune_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    latest_tribune_list={}

try:
    from nation_sports import nation_sports_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    nation_sports_list={}
try:
    from nation_business import nation_business_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    nation_business_list={}
try:
    from nation_entertainment import nation_entertainment_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    nation_entertainment_list={}
try:
    from nation_pakistan import nation_pakistan_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    nation_pakistan_list={}
try:
    from dailyPak_sports import dailyPak_sports_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    dailyPak_sports_list={}
try:
    from dailyPak_business import dailyPak_business_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    dailyPak_business_list={}
try:
    from dailyPak_entertainment import dailyPak_entertainment_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    dailyPak_entertainment_list={}
try:
    from dailyPak_pakistan import dailyPak_pakistan_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    dailyPak_pakistan_list={}
try:
    from dawn_sports import dawn_sports_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    dawn_sports_list={}
try:    
    from dawn_business import dawn_business_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    dawn_business_list={}
try:
    from dawn_entertainment import dawn_entertainment_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    dawn_entertainment_list={}
try:
    from dawn_pakistan import dawn_pakistan_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    dawn_pakistan_list={}
try:
    from pakToday_sports import pakToday_sports_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    pakToday_sports_list={}
try:
    from pakToday_entertainment import pakToday_entertainment_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    pakToday_entertainment_list={}
try:
    from pakToday_business import pakToday_business_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    pakToday_business_list={}
try:
    from pakToday_pakistan import pakToday_pakistan_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    pakToday_pakistan_list={}
try:
    from tribune_sports import tribune_sports_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    tribune_sports_list={}
try:
    from tribune_business import tribune_business_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    tribune_business_list={}
try:
    from tribune_entertainment import tribune_entertainment_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    tribune_entertainment_list={}
try:
    from tribune_pakistan import tribune_pakistan_list
except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
    tribune_pakistan_list={}

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        search_keyword=request.form['searchbar']
        news = search_keyword
        my_data=crawl.detect_news(news)
        print(my_data)
        return render_template('index.html',get_my_data=my_data,get_search_keyword=search_keyword,
        get_latest_nation_list=latest_nation_list,get_latest_dailyPak_list=latest_dailyPak_list,
        get_latest_dawn_list=latest_dawn_list,get_latest_pakToday_list=latest_pakToday_list,
        get_latest_tribune_list=latest_tribune_list)
    elif "id" in session:
        return redirect(url_for("user_index"))
    else:
        return render_template('index.html',
        get_latest_nation_list=latest_nation_list,get_latest_dailyPak_list=latest_dailyPak_list,
        get_latest_dawn_list=latest_dawn_list,get_latest_pakToday_list=latest_pakToday_list,
        get_latest_tribune_list=latest_tribune_list)
@app.route('/user-index',methods=['POST','GET'])
def user_index():
    if request.method=='POST' and "id" in session:
        search_keyword=request.form['searchbar']
        news = search_keyword
        account=session["user"]
        my_data=crawl.detect_news(news)
        print(my_data)
        df = pd.DataFrame.from_dict(my_data,orient='index',columns=['title','description','link','source'])
        df.to_csv('databases/user_databases/news.csv',header=True,index=False)
        get_keywords=request.form['searchbar']
        get_id=session["id"]
        add_search=search_history(search_keywords=get_keywords,user_id=get_id)
        try:
            db.session.add(add_search)
            db.session.commit()
            return render_template('user_index.html',get_my_data=my_data,get_search_keyword=search_keyword,accounts=account)
        except:
            return render_template('user_index.html',get_my_data=my_data,get_search_keyword=search_keyword,accounts=account) 
    elif "user" in session:
        account=session["user"]
        return render_template('user_index.html',accounts=account)
    else:
        return redirect(url_for("signin"))
@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
    if request.method == 'POST' and "id" in session:
        u_id=session["id"]
        get_value=request.form.getlist('checkbox')
        if get_value:
            delete_interest=user_interest.query.filter_by(user_id=u_id).all()
            try:
                for interests in delete_interest:
                    db.session.delete(interests)
                    db.session.commit()
            except:
                return "There was an issue deleting interest"
            for i in get_value:
                add_interest=user_interest(interest_name=i,user_id=u_id)
                try:
                    db.session.add(add_interest)
                    db.session.commit()
                except:
                    return "problem saving"+get_value[i]
            return redirect('/dashboard')
        else:
            delete_interest=user_interest.query.filter_by(user_id=u_id).all()
            try:
                for interests in delete_interest:
                    db.session.delete(interests)
                    db.session.commit()
                return redirect('/dashboard')
            except:
                return "There was an issue deleting history"
    if "id" in session:
        get_id=session["id"]
        keywords=search_history.query.filter_by(user_id=get_id).all()
        get_interests=user_interest.query.filter_by(user_id=get_id).all()
        sports=False
        entertainment=False
        pakistan=False
        business=False
        for i in get_interests:
            if i.interest_name == "sports":
                sports=True
            if i.interest_name == "entertainment":
                entertainment=True
            if i.interest_name == "pakistan":
                pakistan=True
            if i.interest_name == "business":
                business=True
        return render_template('dashboard.html',
        keywords=keywords,sports=sports,entertainment=entertainment,
        business=business,pakistan=pakistan)
    else:
        return redirect(url_for("signin"))
@app.route('/newsfeed')
def newsfeed():
    if "id" in session:
        get_id=session["id"]
        get_interests=user_interest.query.filter_by(user_id=get_id).all()
        sports=False
        entertainment=False
        pakistan=False
        business=False
        for i in get_interests:
            if i.interest_name == "sports":
                sports=True
            if i.interest_name == "entertainment":
                entertainment=True
            if i.interest_name == "pakistan":   
                pakistan=True
            if i.interest_name == "business":
                business=True
        return render_template('newsfeed.html',
        sports=sports,entertainment=entertainment,business=business,pakistan=pakistan,
        get_nation_business_list=nation_business_list,
        get_nation_entertainment_list=nation_entertainment_list,
        get_nation_pakistan_list=nation_pakistan_list,get_nation_sports_list=nation_sports_list,
        get_pakToday_business_list=pakToday_business_list,
        get_pakToday_entertainment_list=pakToday_entertainment_list,
        get_pakToday_pakistan_list=pakToday_pakistan_list,
        get_pakToday_sports_list=pakToday_sports_list,
        get_dawn_business_list=dawn_business_list,
        get_dawn_entertainment_list=dawn_entertainment_list,
        get_dawn_pakistan_list=dawn_pakistan_list,get_dawn_sports_list=dawn_sports_list,
        get_dailyPak_business_list=dailyPak_business_list,
        get_dailyPak_entertainment_list=dailyPak_entertainment_list,
        get_dailyPak_pakistan_list=dailyPak_pakistan_list,
        get_dailyPak_sports_list=dailyPak_sports_list,
        get_tribune_business_list=tribune_business_list,
        get_tribune_entertainment_list=tribune_entertainment_list,
        get_tribune_pakistan_list=tribune_pakistan_list,
        get_tribune_sports_list=tribune_sports_list)
    else:
        return redirect(url_for("signin"))
@app.route('/latest-news')
def latest_news():
    return render_template('latest_news.html',
    get_latest_nation_list=latest_nation_list,get_latest_dailyPak_list=latest_dailyPak_list,
    get_latest_dawn_list=latest_dawn_list,get_latest_pakToday_list=latest_pakToday_list,
    get_latest_tribune_list=latest_tribune_list)
@app.route('/signin',methods=['POST','GET'])
def signin():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        account=user_account.query.filter_by(user_email=email,
        user_password=password).first()
        if account:
            session["user"]=account.user_firstname
            session["id"]=account.user_id
            return redirect('/user-index')
    if "id" in session:
        return redirect('/dashboard')
    else:
        return render_template('signin.html')
@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        password=request.form['password']
        add_user=user_account(user_firstname=first_name,user_lastname=last_name,
        user_email=email,user_password=password)
        try:
            db.session.add(add_user)
            db.session.commit()
            return redirect('/signin')
        except:
            return 'Account already exists.'
    else:
        return render_template('signup.html')
@app.route('/signout')
def signout():
    if "user" in session and "id" in session:
        session.pop("user",None)
        session.pop("id",None)
        return redirect(url_for("index"))
@app.route('/change-name',methods=['POST','GET'])
def change_name():
    if request.method == 'POST':
        get_id=session["id"]
        get_fname=request.form['first_name']
        get_lname=request.form['last_name']
        user=user_account.query.filter_by(user_id=get_id).first()
        user.user_firstname=get_fname
        user.user_lastname=get_lname
        try:
            db.session.commit()
            session["user"]=user.user_firstname
            return redirect('/change-name')
        except:
            return "There was an issue updating data"
    if "id" in session:
        return render_template('change_name.html')
    else:
        return redirect(url_for("signin"))
@app.route('/change-password',methods=['POST','GET'])
def change_password():
    if request.method == 'POST':
        get_id=session["id"]
        get_password=request.form['old_password']
        get_confirm_password=request.form['confirm_new_password']
        user=user_account.query.filter_by(user_id=get_id).first()
        if user.user_password==get_password:
            user.user_password=get_confirm_password
            try:
                db.session.commit()
                return redirect('/change-password')
            except:
                return "There was an issue updating password"
        else:
            return "Your current password is incorrect"
    if "id" in session:
        return render_template('change_password.html')
    else:
        return redirect(url_for("signin"))
@app.route('/delete-account')
def delete_account():
    if "user" in session and "id" in session:
        get_id=session["id"]
        delete_user=user_account.query.filter_by(user_id=get_id).first()
        delete_user_history=search_history.query.filter_by(user_id=get_id).all()
        try:
            db.session.delete(delete_user)
            db.session.commit()
            for users in delete_user_history:
                db.session.delete(users)
                db.session.commit()
            session.pop("user",None)
            session.pop("id",None)
            return redirect(url_for("signin"))
        except:
            return "There was an issue deleting history"
    else:
        return redirect(url_for("signin"))
@app.route('/clear')
def clear():
    if "user" in session and "id" in session:
        get_id=session["id"]
        delete_user_history=search_history.query.filter_by(user_id=get_id).all()
        try:
            for users in delete_user_history:
                db.session.delete(users)
            db.session.commit()
            return redirect('/dashboard')
        except:
            return "There was an issue deleting history"
    else:
        return redirect(url_for("signin"))

@app.route('/save-news')
def download_file():
    return send_file('databases/user_databases/news.csv',mimetype="text/csv",
    as_attachment=True,attachment_filename='news.csv')

if __name__ == "__main__":
    app.run(debug=False)