#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pymongo import MongoClient



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'

db = SQLAlchemy(app)

mongoclient = MongoClient('127.0.0.1', 27017)
mongodb = mongoclient.shiyanlou



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
        self.category = category
        self.content = content


    def __repr__(self):
        return '<File(title=%s)>' %self.title




    def add_tag(self, tag_name):
        file_tags = mongodb.tag.find_one({'file_id': self.id})
        if file_tags == None:
            mongodb.tag.insert_one({'file_id': self.id, 'title':self.title, 'tags':[tag_name]})
        else:
            tags= file_tags['tags']
            tags.append(tag_name)
            tags = set(tags)
            mongodb.tag.update_one({'file_id': self.id},{'$set':{'tags': list(tags)}})





    def remove_tag(self, tag_name):
        file_tags = mongodb.tag.find_one({'file_id': self.id})
        tags= file_tags['tags']
        try:
            tags.remove(tag_name)
        except ValueError:
            return "tag not exist"

        mongodb.tag.update_one({'file_id': self.id},{'$set':{'tags': tags}})
        






    @property
    def tags(self):
        file_tags = mongodb.tag.find_one({'file_id': self.id})
        return file_tags['tags']












db.drop_all()
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


file1.add_tag('tech')
file1.add_tag('Java')
file1.add_tag('linux')
file2.add_tag('tech')
file2.add_tag('Python')



article_list = db.session.query(File.id, File.title).all()

print(article_list)



@app.route('/')
def index():
    article_list = db.session.query(File.id, File.title).all()
    l =[]
    for article in article_list:
        article = list(article)
        f = File.query.get(article[0])
        article.append(f.tags)
        l.append(article)

    article_list = l


    return render_template("index.html", article_list = article_list)




@app.route('/files/<fileid>')


def file(fileid):
    file = File.query.get_or_404(fileid)

    return render_template('file.html', file = file)



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404




if __name__ == '__main__':
    app.run()


