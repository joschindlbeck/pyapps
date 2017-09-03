'''
Created on 03.09.2017

@author: josch
'''

from flask import Flask
app = Flask(__name__)

@app.route("/HelloWorldGit")
def hello():
    return "Hello World, transferred by GITHub"
