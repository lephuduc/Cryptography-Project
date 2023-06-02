from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Products(db.Model):
    id = db.Column(db.String(5), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(), nullable=True)
    category = db.Column(db.String(50), nullable=False)
    sold = db.Column(db.Integer, nullable=False,default=0)
    date = db.Column(db.DateTime, default=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))


# id='DI001',name='Diamond 01', price='1000', sold='20', desc='This is a diamond', category='Diamond'
# id='GO001',name='Gold 01', price='500', sold='99', desc='This is gold', category='Gold'