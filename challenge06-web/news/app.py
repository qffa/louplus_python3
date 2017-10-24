#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template
import os
import json



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    article_list = []
    filenames = os.listdir('../files')

    for filename in filenames:
        filename = '../files/' + filename
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                article = json.loads(f.read())
                article_list.append(article['title'])


    return render_template("index.html", article_list = article_list)



@app.route('/files/<filename>')
def file(filename):
    pass







@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404





if __name__ == '__main__':
    app.run()
