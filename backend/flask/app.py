from startup import app
from flask import request

import endpoints_account


@app.route('/', methods=['GET', 'POST'])
def parse_request():
    data = request.json # data is empty
    print (data)
    return data
    
    
@app.route('/user', methods=['GET', 'POST'])
def parse_request():
    data = request.json # data is empty
    print (data)
    return data
    
    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"