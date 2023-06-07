import requests
import os

# config URL here
URL_SECURITY_SERVICE = f'http://{os.getenv("SECURITY_SVC_ADDRESS")}'

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
        return respone
        # token = respone['token']
        # username = respone['username']
        # print(respone)
    except:
        return False
