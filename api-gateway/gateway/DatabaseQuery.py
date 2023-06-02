import sqlite3
from werkzeug.security import check_password_hash
import bcrypt

def submit_user(username,password,email):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    conn = sqlite3.connect('Users')
    cursor = conn.cursor()
    #check if username already exists
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    result = cursor.fetchone()
    if result is not None:
        return "User name already exists"
    #check if email already exists
    cursor.execute("SELECT * FROM Users WHERE email = ?", (email,))
    result = cursor.fetchone()
    if result is not None:
        return "This email has been used"
    #insert userinfor into database
    sql = "INSERT INTO Users (username, password,email) VALUES (?, ?, ?)"
    val = (username, hashed_password,email)
    cursor.execute(sql, val)
    conn.commit()

def validate_password(username, password):
    conn = sqlite3.connect('Users')
    c = conn.cursor()
    c.execute("SELECT password FROM Users WHERE username = ?", (username,))
    result = c.fetchone()
    if result is None:
        return False
    stored_password  = result[0]
    conn.close()
    #hash this password using stored salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), stored_password)
    if hashed_password == stored_password:
        return True
    else:
        return False
