import os
from flask import Flask

application = Flask(__name__)

@application.route('/')
def root():
    return("Hello there")

if __name__ == "__main__":
    application.run()
