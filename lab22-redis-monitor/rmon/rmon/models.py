""" rmon.models

该模块实现了所有的model类以及相应的序列化类

"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Server(db.Model):
    """ Redies服务器模型

    """


    __tablename__ = 'redis_server'
    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String(64), unqiue=True)
    description = db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Integer, default=6379)
    password = db.Column(db.String())
    update_at = db.Column(db.DateTime, default=datetime.utcnow)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Server(name=%s)>' %self.name


    def save(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()




