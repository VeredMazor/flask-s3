import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask,render_template, flash,request ,redirect, Response
import secrets
#import requests
import boto3
from dotenv import load_dotenv


load_dotenv()

s3 = boto3.client('s3')

img_url = s3.generate_presigned_url('get_object',Params={'Bucket': os.getenv("S3NAME"),'Key': os.getenv("IMAGE")})



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
SECRET_KEY = secrets.token_hex(16)

db = SQLAlchemy(app)


#migrate = Migrate(app, db)





class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        user = User.query.filter_by(username=username, email=email).first()
        if user:
            return redirect('/home/' + username)
        else:
            flash("Invalid credentials, please try again.")
            return render_template('signin.html')
    else:
        return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['email']
            print(username)
            print(email)
            user = User.query.filter_by(username=username).first()
            if user:
                flash("User already exists")
                return render_template('signup.html')
            user_obj = User(username=username, email=email)
            db.session.add(user_obj)
            db.session.commit()
            return redirect('/home/' + username)
        except Exception as e:
            error = str(e)
            flash(error, 'error')
            return render_template('signup.html')
    else:
        return render_template('signup.html')



            

@app.route('/home/<username>', methods=['GET', 'POST'])
def home(username):
    #print(img_url)
    return render_template('home.html',name=username, img=img_url)



@app.route('/logout')
def logout():
    os.environ.pop('AWS_ACCESS_KEY_ID', None)
    os.environ.pop('AWS_SECRET_ACCESS_KEY', None)
    os.environ.pop('AWS_SESSION_TOKEN', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
