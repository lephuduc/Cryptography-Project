from flask import Flask, request, render_template, redirect, abort, url_for, send_from_directory, make_response
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from models import *
import os
import json
import re
import jwt
from conf import settings

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRESSQL_URI")
db.init_app(app)
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


@app.route('/api/signin', methods=['POST'])
def signin():
    username = request.form.get('username', '')
    if not re.match("^[a-zA-Z0-9_]{1,200}$", username):
        return json.dumps({"status":"The username should match this regular expression '^[a-zA-Z0-9_]{1,200}$'","status_code":500})
    user = User.query.filter_by(name=username).first()
    if not user:
        return json.dumps({"status":"Invalid username", "status_code":404})
    if not check_password_hash(user.password, request.form.get('password', '')):
        return json.dumps({"status":"Invalid password", "status_code":403})
    ret = {"username":username,"token": genenrate_token(username)}
    return json.dumps(ret)

def genenrate_token(
        name:str,
        expires_delta: timedelta = timedelta(
            minutes=settings.ACCESS_TOKEN_DEFAULT_EXPIRE_MINUTES
        )
):
    expire = datetime.utcnow() + expires_delta
    token_data = {
        'username': name,
        'exp': expire
    }
    encoded_jwt = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.route('/api/signup', methods=['POST'])
def signup():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    email = request.form.get('email')
    if not (username and password and email):
        return json.dumps({"status":"You have to specify username *and* password *and* email"})

    if not re.match("^[a-zA-Z0-9_]{1,200}$", username):
        return json.dumps({"status":"The username should match this regular expression '^[a-zA-Z0-9_]{1,200}$'","status_code":500})
    user = User.query.filter_by(name=username).first()
    try:
        attributes = '{"user_role": "user","department": "None","location": "None"}'
        user = User(username, generate_password_hash(password),email,attributes)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(e)
        return json.dumps({"status":"Username already taken"})
    return json.dumps({"status":"User sign up sucessfully, please return to login"})

@app.route('/api/author', methods=['POST'])
def author():
    cookies = request.cookies
    token_encoded = cookies.get('session_token')
    if not token_encoded:
        json.dumps({"status":"Missing credentials","status_code":401})
    token_data = jwt.decode(token_encoded,SECRET_KEY,ALGORITHM)
    username = token_data['username']
    exp = token_data['exp']
    if exp<datetime.timestamp(datetime.now()):
        return json.dumps({'status':"Session expired, please login again."})
    return json.dumps({"user":username})  


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(host='0.0.0.0', port=5002)
