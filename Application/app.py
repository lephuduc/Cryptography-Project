from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    url_for,
    session)
from DatabaseQuery import validate_password,submit_user
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
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
    if request.method=='POST':
        username,password,retype_password,email = request.form["username"],request.form["password"],request.form["retype_password"],request.form["email"]
        if retype_password!=password:
            return render_template('register.html',error = "Password does not match")
        error = submit_user(username,password,email)
        if error!=None:
             return render_template('register.html',error = error)
        return render_template('login.html',anouce = "Resgiter successfully")
    return render_template('register.html')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)