from startup import app, db
from flask import request
import _account
import algorithms

import endpoints_account


@app.route('/oras', methods=['GET', 'POST'])
def endpoint():
    dat=algorithms.oras()
    return dat

@app.route('/sievo', methods=['GET', 'POST'])
def endpoint():
    dat=algorithms.sievo()
    return dat

@app.route('/elisa', methods=['GET', 'POST'])
def endpoint():
    dat=algorithms.elisa()
    return dat

@app.route('/vikes', methods=['GET', 'POST'])
def endpoint():
    dat=algorithms.vikes()
    return dat
