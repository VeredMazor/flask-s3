import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask,render_template, flash,request ,redirect, Response
import secrets
#import requests
import boto3




s3 = boto3.client('s3')

#img_url = s3.generate_presigned_url('get_object',Params={'Bucket': os.getenv("S3NAME"),'Key': 'shih-tzu-dog.jpeg'})



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
SECRET_KEY = secrets.token_hex(16)

db = SQLAlchemy(app)


#migrate = Migrate(app, db)





class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            print(username)
            print(password)
            user = User.query.filter_by(username=username).first()
            if user:
                flash("user is exists")
                return render_template('signup.html')
            user_obj = User(username=username, password=password)
            db.session.add(user_obj)
            db.session.commit()
            return redirect('/home')
        except Exception as e:
            error = str(e)
            #flash(error, 'error')
        # After processing the POST request, return the template
        return redirect('/home')
    else:
        # For GET requests, simply render the template
        return render_template('signup.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.method.form['username']
        password = request.method.form['password']
        user = User(username=username, password=password)
        if user:
            return redirect('/home')
        else:
            return render_template('signin.html')
    else:
        return render_template('signin.html')
        
            

@app.route('/home', methods=['GET', 'POST'])
def home():
    print(img_url)
    return render_template('home.html', video_url="/video")



@app.route('/video')
def video():
    # Presuming you have AWS credentials set up in your environment or using IAM roles in EC2
    bucket_name = 'vered-mazor-s3'
    video_file = "shih-tzu-dog.jpeg"
    video_object = s3.get_object(Bucket=bucket_name, Key=video_file)
    return Response(
        video_object['Body'].read(),
        mimetype='jpeg',
        headers={
            "Content-Disposition": "inline; filename={}".format(video_file)
        }
    )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
