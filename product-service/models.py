from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Products(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(500),nullable=True)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(500), nullable=False)
    sold = db.Column(db.Integer, nullable=False,default=0)


# id='DI001',name='Diamond 01', price='1000', sold='20', desc='This is a diamond', category='Diamond'
# id='GO001',name='Gold 01', price='500', sold='99', desc='This is gold', category='Gold'