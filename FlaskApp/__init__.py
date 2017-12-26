from flask import Flask
app = Flask(__name__)

import FlaskApp.views
from WeiXinCore.WeiXin import echo
#try:
    import os
    import FlaskApp.os_py
#except:
#    print("no in os.")
