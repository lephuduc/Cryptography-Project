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

@app.route('/api/insert_product', methods=['POST'])
def insert_product():
    products_json = request.get_json()

    if not isinstance(products_json, list):
        return json.dumps({"status":"Invalid payload format. Expected a list of products","status_code":"400"})

    new_products = []
    status = []
    for product in products_json:
        try:
            new_product = Products(
                id=product.get('id'),
                title=product.get('title'),
                image=product.get('image'),
                price=product.get('price'),
                category=str(product.get('category')).replace("'",'"')
            )
            new_products.append(new_product)
        except:
            status.append({"status":f"Bad Req {id}","status_code":"400"})
    
    db.session.add_all(new_products)
    db.session.commit()
    status.append({"status":"Products inserted successfully","status_code":"200"})
    return json.dumps(status)

@app.route('/api/delete_product', methods=['POST'])
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

@app.route('/api/allproduct',methods=['GET'])
def get_all_products():
    products = Products.query.all()
    product_list  = [product.__dict__ for product in products]
    for product in product_list:
        product.pop('_sa_instance_state')
    return json.dumps(product_list,default=str)

# @app.route('/api/bestseller',methods=['GET'])
# def get_best_seller():
#     products = Products.query.all()
#     product_list  = [product.__dict__ for product in products]
#     for product in product_list:
#         product.pop('_sa_instance_state')
#     best_seller_list = sorted(product_list, key=itemgetter('sold'),reverse=True)
#     print(best_seller_list)
#     return json.dumps(best_seller_list,default=str)

# @app.route('/api/newest',methods=['GET'])
# def get_new():
#     products = Products.query.all()
#     product_list  = [product.__dict__ for product in products]
#     for product in product_list:
#         product.pop('_sa_instance_state')
#     best_seller_list = sorted(product_list, key=itemgetter('date'),reverse=True)
#     print(best_seller_list)
#     return json.dumps(best_seller_list,default=str)

if __name__ == '__main__':
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    app.run(host='0.0.0.0', port=5003)