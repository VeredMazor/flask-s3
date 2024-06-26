# Flask Web Application with AWS S3 Integration and EC2 Integration(Load Balancer & Auto Scaling Group)
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
cd flask-s3 https://github.com/VeredMazor/flask-s3.git
docker build -t myapp .
docker run -d -p 5555:5555 myapp
```

### Images
Sign in:
<img width="1512" alt="Sign in" src="https://github.com/VeredMazor/flask-s3/assets/72979004/f2ab854e-208a-4a17-a60c-25fc6accc1cc">
Sign up:
<img width="1512" alt="Sign up" src="https://github.com/VeredMazor/flask-s3/assets/72979004/a6f20836-bee9-41d8-8891-83b94a72b615">
Home:
<img width="1507" alt="Home" src="https://github.com/VeredMazor/flask-s3/assets/72979004/6b476ad8-11cd-4918-9dfd-9754950c3c54">
### Auto scaling template
```
#!/bin/bash

# Clone the project repository
git clone "https://github.com/VeredMazor/flask-s3.git"

# Update package lists and install Docker
sudo apt-get update
sudo apt-get install docker.io -y

# Start Docker service
sudo systemctl start docker

# Navigate to the project directory
cd myapp/

# Set up environment variables in .env file
echo "S3NAME=YOUR_BUCKET_NAME" >> .env
echo "IMAGE=YOUR_IMAGE_NAME" >> .env

# Build Docker image for Flask app
sudo docker build -t myapp .

# Run and open the container to port 5555
sudo docker run -p 5555:5555  myapp
```

Home with load balancer and auto scaling group:
<img width="1512" alt="Home with load balancer" src="https://github.com/VeredMazor/flask-s3/assets/72979004/01d9ada7-1203-4458-8d42-3ec32cd19186">

### Commands to apply pressure to add more EC2 instance with auto scaling group
```bash
sudo apt-get install stress-ng

stress-ng --cpu $(nproc) --timeout 5m --metrics-brief
```

### License
This project is licensed under the MIT License. See the LICENSE file for details.
