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

    def __repr__(self):
        return "<Post(title='%s')>" %self.title





class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Category(name=%s)>" %self.name



db.drop_all()
db.create_all()


py = Category("Python")
ja = Category("Java")
p1 = Post("hello python", "Python is cool!", py)
p2 = Post("hello Java", "Java is cool!", ja)
db.session.add(py)
db.session.add(ja)
db.session.add(p1)
db.session.add(p2)


db.session.commit()


#print(db.session.query(Post.title).all())

#print(db.session.query(Post).filter(Post.id == 1).first())
p = db.session.query(Post).join(Category, Post.category_id == Category.id).first()

print(p.category.name)
