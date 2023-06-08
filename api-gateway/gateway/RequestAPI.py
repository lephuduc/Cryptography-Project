import requests
import os

# config URL here
URL_SECURITY_SERVICE = f'http://{os.getenv("SECURITY_SVC_ADDRESS")}'
URL_SECURITY_SERVICE = 'http://187.125.84.102:5002'
def submit_user(username,password,email):
    data = {"username":username,"password":password,"email":email}
    req = requests.post(URL_SECURITY_SERVICE+"/api/signup",data=data)
    respone = req.json()
    status = respone['status']
    return status

def validate_password(username, password):
    data = {"username":username,"password":password}
    req = requests.post(URL_SECURITY_SERVICE+"/api/signin",data=data)
    respone = req.json()
    try:
        token = respone['token']
        username = respone['username']
        return respone
    except:
        return False
def is_logged_in(token_encoded):
    if token_encoded:
        cookies = {'session_token':token_encoded}
        req = requests.post(URL_SECURITY_SERVICE+"/api/author",cookies=cookies)
        respone = req.json()
        try:
            username = respone['user']
            return True
        except:
            return False
    return False
