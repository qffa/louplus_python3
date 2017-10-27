#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'

db = SQLAlchemy(app)


class Category(db.Model):
#    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return "<Category(name=%s)>" %self.name


class File(db.Model):
#    __tablename__ = "file"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref='files')
    content = db.Column(db.Text)


    def __init__(self, title, time, category, content):
        self.title = title
        self.created_time = time
        self.categorg = category
        self.content = content


    def __repr__(self):
        return '<File(title=%s)>' %self.title


db.create_all()


java = Category('Java')
python = Category('Python')

file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')

db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)

db.session.commit()




@app.route('/')
def index():
    article_list = []
    filenames = os.listdir('../files')

    for filename in filenames:
        filepath = '../files/' + filename
        if os.path.isfile(filepath):
            with open(filepath, 'r') as f:
                article = json.loads(f.read())
                article_list.append(article['title'])


    return render_template("index.html", article_list = article_list)



@app.route('/files/<filename>')
def file(filename):
    filepath = '../files/' + filename + '.json'
    if os.path.isfile(filepath):
        with open(filepath, 'r') as f:
            article = json.loads(f.read())

        return render_template('file.html', article = article)

    else:
        return render_template('404.html'), 404


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404



'''

if __name__ == '__main__':
    app.run()


'''
