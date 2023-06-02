from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
from json import dump, dumps, loads
import subprocess

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRESSQL_URI")

db = SQLAlchemy(app)

class User(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100),nullable = False)
    attributes = db.Column(db.String(300),nullable = False)
    def __init__(self, name, password,email,attributes):
        self.name = name
        self.password = password
        self.email = email
        self.attributes = attributes

@app.route('/api/v1/opa', methods=['POST'])
def exec_abac():
    request_dict = request.get_json()
    username = request_dict["user"]
    operations = {"user": username}
    with open('users.json', 'w') as f:
        d = {"user_attributes": { username: get_attr(username)}}
        print(d)
        dump(d, f)
    with open('input.json', 'w') as f:
        dump(operations, f)
    
    # run opa
    
    command = "./opa eval -d resources.json -d users.json -d policy.rego --input input.json 'data.abac.allow' --format raw"
    
    output = subprocess.check_output(command, shell=True, encoding="utf-8").strip()
    
    return {'result': output}
    
def get_attr(username):
    user = User.query.filter_by(name=username).first()
    
    return loads(user.attributes)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181)
