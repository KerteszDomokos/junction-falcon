from startup import app

import endpoints_account

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"