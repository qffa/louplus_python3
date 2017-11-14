""" rmon.app

��ģ����Ҫʵ����app��������

"""

import os
from flask import Flask
from rmon.views import api
from rmon.models import db
from rmon.config import DevConfig, ProductConfig


def create_app():
    """ ��������ʼ��Flask app

    """

    app = Flask('rmon')

    #���ݻ����������ؿ�����������������������
    env = os.environ.get('RMON_ENV')
    if env in ('pro', 'prod', 'product'):
        app.config.from_object(ProductConifg)
    else:
        app.config.from_object(DevConfig)

    #�ӻ�������RMON_SETTINGSָ�����ļ��м�������
    app.config.from_envvar('RMON_SETTINGS', silent=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIOINS'] = False


    #ע�� Blueprint
    app.register_blueprint(api)
    #��ʼ�����ݿ�
    db.init_app(app)
    #����ǿ��������򴴽��������ݿ��
    if app.debug:
        with app.app_context():
            db.create_all()
    return app








