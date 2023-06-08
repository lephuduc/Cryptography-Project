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
import requests
from json import dumps, loads
from RequestAPI import validate_password,submit_user,is_logged_in


load_dotenv()
app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    cookies = request.cookies
    token_encoded = cookies.get('session_token')
    if is_logged_in(token_encoded):
        return render_template('login.html',anouce = 'User already logged in')
    if request.method=='POST':
        username,password = request.form["username"], request.form["password"]
        check_respone = validate_password(username,password)
        if not check_respone:
            error_msg = "Invalid password or username"
            return render_template('login.html',error = error_msg)
        else:
            token = check_respone['token']
            username = check_respone['username']
            response = make_response(render_template('login.html',anouce = 'User sign in successfully'))
            response.set_cookie('session_token',value=token,max_age=3600)
            return response
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    global redirect_from_register
    if request.method=='POST':
        username,password,retype_password,email = request.form["username"],request.form["password"],request.form["retype_password"],request.form["email"]
        if retype_password!=password:
            return render_template('register.html',error = "Password does not match")
        status = submit_user(username,password,email)
        if status!="User sign up sucessfully, please return to login":
            return render_template('register.html',error = status)
        return render_template('register.html',anouce = status)
    return render_template('register.html')

# Route for the root URL ("/")
@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html', title="Jelwery")

# Route for /products/
@app.route('/products/', methods=['GET'])
def product_page():
    api_url = f"http://{os.getenv('PRODUCT_SVC_ADDRESS')}/api/allproduct"
    products = requests.get(api_url).json()
    file_path = f"./static/json/products.json"
    with open(file_path,'w') as f:
        f.write(products)
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
    api_url = f"http://{os.getenv('ABOUT_SVC_ADDRESS')}/api/getAbout"
    response = requests.get(api_url)
    data = response.json()
    return render_template('about.html', title="About us", about_list=loads(data))

@app.route('/cart/', methods=['GET'])
def cart_page():    
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

@app.route("/api/v1/updateAbout", methods=["POST"])
def update_about_api_handler():
    # Authentication
    ## /api/author
    cookie = request.cookies
    authResponse = requests.post(f"http://{os.getenv('SECURITY_SVC_ADDRESS')}/api/author")
    if authResponse.status_code in (401, 422, 440):
        return authResponse
    
    # Authorization
    ## /api/v1/opa
    dataOpa = authResponse.json()
    opaUri = f"http://{os.getenv('OPA_SVC_ADDRESS')}/api/v1/opa"
    opaResponse = requests.post(opaUri, data=dataOpa)
    jsonOpa = opaResponse.json()
    if jsonOpa["result"] == "true":
        aboutSVCResponse = requests.post(f"http://{os.getenv('ABOUT_SVC_ADDRESS')}/api/updateAbout",
                                         data=request.json)    
    
        return aboutSVCResponse
    else:
        return jsonify({"result": "Your are not allowed to update"})

if __name__ == '__main__':
    app.run(host="0.0.0.0")
