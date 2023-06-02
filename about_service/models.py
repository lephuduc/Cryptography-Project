from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    description = db.Column(db.Text)
    __tablename__ = 'about'
