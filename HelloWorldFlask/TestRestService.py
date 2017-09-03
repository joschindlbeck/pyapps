'''
Created on 03.09.2017

@author: josch
'''

from flask import Flask, jsonify, json

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://wutuser:test@localhost/wut4lunch'

db = SQLAlchemy(app)


@app.route("/testrestservice", methods=['GET'])
def get_users():
        userlist = User.query.all()
        strUserlist = str(userlist)
        return jsonify(strUserlist)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    comment = db.Column(db.String(120), unique=False)

    def __init__(self, username, email, comment):
        self.username = username
        self.email = email
        self.comment = comment

    def __repr__(self):
        return json.dumps(self)
        #return jsonify(self)
    
