from flask import Flask, jsonify, request, render_template, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from RequestAPI import validate_password,submit_user


load_dotenv()
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("POSTGRESSQL_URI")
# db = SQLAlchemy(app)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username,password = request.form["username"], request.form["password"]
        if not validate_password(username,password):
            error_msg = "Invalid password or username"
            return render_template('login.html',error = error_msg)
        else:
            return redirect(url_for('main_page'))
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    global redirect_from_register
    if request.method=='POST':
        username,password,retype_password,email = request.form["username"],request.form["password"],request.form["retype_password"],request.form["email"]
        if retype_password!=password:
            return render_template('register.html',error = "Password does not match")
        status = submit_user(username,password,email)
        if status!="User sign up sucessfully!":
             return render_template('register.html',error = status)
        return render_template('register.html',anouce = status)
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
def server_image(file_name):
    if allowed_file(file_name):
        return send_from_directory('static/images', file_name, mimetype=f'image/{file_name.rsplit(".", 1)[1]}')
    else:
        return 'Invalid image format', 404

@app.route('/about/', methods=['GET'])
def about_page():
    # TODO: query the data from about service api
    return render_template('about.html', title="About us")

# Route for handling invalid URLs
@app.errorhandler(404)
def page_not_found(error):
    # Redirect to the root URL ("/")
    return redirect(url_for('main_page'))


if __name__ == '__main__':
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    #     insert_about()
    app.run(host="0.0.0.0")
