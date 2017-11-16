""" rmon.model

该模块实现了所有的model类以及相应的序列化类
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from redis import StrictRedis, RedisError
from rmon.common.rest import RestException
from marshmallow import (Schema, fields, validate, post_load, validates_schema, ValidationError)


db = SQLAlchemy()

class Server(db.Model):
    """
    Redies服务器模型
    """


    __tablename__ = 'redis_server'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Integer, default=6379)
    password = db.Column(db.String())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Server(name=%s)>' %self.name



    def save(self):
        db.session.add(self)
        db.session.commit()



    def delete(self):
        db.session.delete(self)
        db.session.commit()



    def ping(self):
        """ 检查服务器是否可以访问

        """

        try:
            return self.redis.ping()
        except RedisError:
            raise RestException(400, 'redis server %s can not connected' %self.host)



    def get_metrics(self):
        """获取Redis服务器监控信息

        通过Redis服务器指令INFO返回监控信息，参考https://redis.io/commands/INFO
        """

        try:
            return self.redis.info()
        except RedisError:
            raise RestException(400, 'redis server %s can not connected' %self.host)



    @property
    def redis(self):
        return StrictRedis(host=self.host, port=self.port, password=self.password)



class ServerSchema(Schema):
    """ Redis服务器记录序列化类

    """

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(2,64))
    description = fields.String(validate=validate.Length(0,512))
    host = fields.String(required=True, validate=validate.Regexp(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'))
    port = fields.Integer(validate=validate.Range(1024, 55536))
    password = fields.String()
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

    @validates_schema
    def validate_schema(self, data):
        """验证是否已经存在同名Redis服务器

        """
        if 'port' not in data:
            data['port'] = 6379

        instance = self.context.get('instance', None)
        server = Server.query.filter_by(name=data['name']).first()

        if server is None:
            return

        if instance is not None and server != instance:
            raise ValidationError('Redis server already exist', 'name')


    @post_load
    def create_or_update(self, data):
        """数据加载成功后自动创建Server对象

        """

        instance = self.context.get('instance', None)

        if instance is None:
            return Server(**data)

        for key in data:
            setattr(instance, key ,data[key])

        return instance



