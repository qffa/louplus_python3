#!/usr/bin/env python3


# used for test DB function



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app =Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root@localhost/shiyanlou'

db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref = 'posts')


    def __init__(self, title, body, category, pub_date = None):
        self.title = title
        self.body = body
        self.category = category
        if pub_date == None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date



class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category(name=%s)>" %self.name


db.create_all()


py = Category("Python")
p = Post("hello python", "Python is cool!", py)

db.session.add(py)
db.session.add(p)

db.session.commit()
