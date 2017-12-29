#from flask import Flask
#app = Flask(__name__)
#
#@app.route("/")
#def hello():
#    return "Hello World!"
#    
#from WeiXinCore.WeiXin import echo
#
#from flask import Flask, g, request
#
#@app.route('/douban', methods=['GET', 'POST'])
#def douban():
#    return str( dict(request.args))
#  
#@app.route('/fankui', methods=['GET', 'POST'])
#def greeting():
#    html = ''
#
#    return html

from FlaskApp import app, os_py

if __name__ == "__main__":
    application.run()
