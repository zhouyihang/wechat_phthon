import os

from flask import Flask, g, request
from FlaskApp import  app
#app = Flask(__name__)
#app.debug = True

@app.route('/douban', methods=['GET', 'POST'])
def douban():
    return str( dict(request.args))
  



@app.route('/fankui', methods=['GET', 'POST'])
def greeting():
    html = ''

    return html
