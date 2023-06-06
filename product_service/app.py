from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models import *
import os
import json
from operator import itemgetter

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRESSQL_URI")
db.init_app(app)
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# @app.route('/product/api/createdb',methods=['GET'])
# def createdb():
#     product1 = Products(id='DI001',name='Diamond 01', price='1000', sold='20', desc='This is a diamond', category='Diamond',date=datetime(2023, 5, 26, 16, 25, 55))
#     product2 = Products(id='GO001',name='Gold 01', price='500', sold='99', desc='This is gold', category='Gold')
#     db.session.add(product1)
#     db.session.add(product2)
#     db.session.commit()
#     return json.dumps({"return":"added to database"})

@app.route('/product/api/insert_product', methods=['POST'])
def insert_product():
    products_json = request.get_json()

    if not isinstance(products_json, list):
        return json.dumps({"status":"Invalid payload format. Expected a list of products","status_code":"400"})

    new_products = []
    for product in products_json:
        try:
            new_product = Products(
                id=product.get('id'),
                name=product.get('name'),
                price=product.get('price'),
                desc=product.get('desc'),
                category=product.get('category')
            )
            new_products.append(new_product)
        except:
            json.dumps({"status":"Product ID is already taken","status_code":"400"})
    
    db.session.add_all(new_products)
    db.session.commit()

    return json.dumps({"status":"Products inserted successfully","status_code":"200"})

@app.route('/product/api/delete_product', methods=['POST'])
def delete_product():
    products_json = request.get_json()
    status = []
    if not isinstance(products_json, list):
        return json.dumps({"status":"Invalid payload format. Expected a list of id of products","status_code":"400"})

    for product_ids in products_json:
        try:
            get_id=product_ids.get('id')
            product_query = Products.query.get(get_id)
            print(product_query)
            if(product_query == None):
                raise Exception
            else:
                Products.query.filter_by(id=get_id).delete()
                status.append({"status":f"Product ID {get_id} deleted successfully","status_code":"200"})
        except:
            status.append({"status":f"Product ID {get_id} not found","status_code":"404"})
        
        db.session.commit()

    return status

@app.route('/product/api/allproduct',methods=['GET'])
def get_all_products():
    products = Products.query.all()
    product_list  = [product.__dict__ for product in products]
    for product in product_list:
        product.pop('_sa_instance_state')
    print(product_list)
    return json.dumps(product_list,default=str)

@app.route('/product/api/bestseller',methods=['GET'])
def get_best_seller():
    products = Products.query.all()
    product_list  = [product.__dict__ for product in products]
    for product in product_list:
        product.pop('_sa_instance_state')
    best_seller_list = sorted(product_list, key=itemgetter('sold'),reverse=True)
    print(best_seller_list)
    return json.dumps(best_seller_list,default=str)

@app.route('/product/api/newest',methods=['GET'])
def get_new():
    products = Products.query.all()
    product_list  = [product.__dict__ for product in products]
    for product in product_list:
        product.pop('_sa_instance_state')
    best_seller_list = sorted(product_list, key=itemgetter('date'),reverse=True)
    print(best_seller_list)
    return json.dumps(best_seller_list,default=str)

if __name__ == '__main__':
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    app.run(host='0.0.0.0', port=5003)
