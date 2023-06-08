from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

