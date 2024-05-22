# Flask Web Application with AWS S3 Integration
### Overview
This project is a Flask-based web application that allows users to sign up, sign in, and view a home page with an image retrieved from an AWS S3 bucket. The application uses SQLAlchemy for database management and Flask-Migrate for handling database migrations. User credentials are securely managed, and session management is implemented to ensure user security.

### Features
* User registration and authentication
* Integration with AWS S3 to display an image on the home page
* Database management using SQLAlchemy
* Secure handling of environment variables using python-dotenv


### Requirements

The application depends on several Python packages. These are listed in the requirements.txt file:


```plaintext
alembic==1.13.1
blinker==1.8.2
boto3==1.20.54
botocore==1.23.54
click==8.1.7
Flask==3.0.3
Flask-Migrate==4.0.7
Flask-SQLAlchemy==3.1.1
itsdangerous==2.2.0
Jinja2==3.1.4
jmespath==0.10.0
Mako==1.3.5
MarkupSafe==2.1.5
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
s3transfer==0.5.2
six==1.16.0
SQLAlchemy==2.0.30
typing_extensions==4.11.0
urllib3==1.26.18
Werkzeug==3.0.3
Installation
```

## EC2
### Install Docker on Ubuntu in AWS
```bash
sudo apt-get update
sudo apt-get install docker.io -y
sudo systemctl start docker
```
### Create container with app
```bash
mkdir myapp
git clone
cd flask-s3
docker build -t myapp .
docker run -d -p 5555:5555 myapp
```

License
This project is licensed under the MIT License. See the LICENSE file for details.
