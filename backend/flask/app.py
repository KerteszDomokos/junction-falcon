from startup import app, db
from flask import request
import _account

import endpoints_account


@app.route('/', methods=['GET', 'POST'])
def parse_request():
    data = request.json # data is empty
    print (data)
    
    return data
    
    
@app.route('/user', methods=['GET', 'POST'])
def usercreate():
    user=_account.create_user(request.json)
    return user.email
    
    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"