'''
Created on 03.09.2017

@author: josch
'''

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://wutuser:test@localhost/wut4lunch'

db = SQLAlchemy(app)

@app.route("/wut4lunch")
def hello():
        db.create_all()
        admin = User('admin', 'admin@example.com', "Kommentar")
        user1 = User('user1', 'user1@example.com', "Erster User")
        db.session.add(admin)
        db.session.add(user1)
        db.session.commit()
        return "Finished!"

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
        return '<User %r>' % self.username
