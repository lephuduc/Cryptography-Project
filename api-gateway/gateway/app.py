from flask import (Flask, 
                   jsonify, 
                   request, 
                   render_template, 
                   redirect, 
                   url_for, 
                   send_from_directory, 
                   make_response,
                   abort)
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from DatabaseQuery import validate_password,submit_user
import requests
import threading
import subprocess
from json import dumps, loads


load_dotenv()
app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username,password = request.form["username"], request.form["password"]
        if not validate_password(username,password):
            error_msg = "Invalid password or username"
            return render_template('login.html',error = error_msg)
        else:
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    global redirect_from_register
    if request.method=='POST':
        username,password,retype_password,email = request.form["username"],request.form["password"],request.form["retype_password"],request.form["email"]
        if retype_password!=password:
            return render_template('register.html',error = "Password does not match")
        error = submit_user(username,password,email)
        if error!=None:
             return render_template('register.html',error = error)
        return render_template('register.html',anouce = "Resgiter successfully. Returning to login page...")
    return render_template('register.html')

# Route for the root URL ("/")
@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html', title="Shop")

# Route for /products/
@app.route('/products/', methods=['GET'])
def product_page():
    return render_template('products.html', title="Products")

# Route for /contact
@app.route('/contact/', methods=['GET'])
def contact_page():
    return render_template('contact.html', title="Contact")

@app.route('/json/<json_name>')
def get_json_data(json_name):
    # Read the JSON file based on the variable in the URL
    file_path = f"./static/json/{json_name}"
    with open(file_path) as file:
        data = file.read()
    return jsonify(data)


ALLOWED_EXTENSIONS = {'webp', 'jpg', 'jpeg', 'png'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/static/images/<path:file_name>')
def serve_image(file_name):
    if allowed_file(file_name):
        return send_from_directory('static/images', file_name, mimetype=f'image/{file_name.rsplit(".", 1)[1]}')
    else:
        return 'Invalid image format', 404

@app.route('/about/', methods=['GET'])
def about_page():
    api_url = f"http://{os.getenv('ABOUT_SVC_ADDRESS')}/api/getAbout"
    response = requests.get(api_url)
    data = response.json()
    return render_template('about.html', title="About us", about_list=loads(data))

@app.route('/cart/', methods=['GET'])
def cart_page():
    if 
    
    return render_template('cart.html', title="Your cart")

# Route for handling invalid URLs
@app.errorhandler(404)
def page_not_found(error):
    # Redirect to the root URL ("/")
    return redirect(url_for('main_page'))

@app.route("/api/v1/getAbout/", methods=['GET'])
def get_about_api_handler():
    api_url = f"http://{os.getenv('ABOUT_SVC_ADDRESS')}/api/getAbout"
    
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    
    return make_response("Not found", status=404)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
