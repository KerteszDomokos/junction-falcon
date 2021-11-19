from startup import app, db
from flask import request
import _account
import algorithms

import endpoints_account


@app.route('/oras', methods=['GET', 'POST'])
def endpoint():
    dat=algorithms.oras()
    return dat
    
    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"