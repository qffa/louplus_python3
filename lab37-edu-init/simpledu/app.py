from flask import Flask, render_template
from simpledu.config import configs
from simpledu.models import db, Course


def create_app(config):
    """ APP 工厂

    """

    app = Flask(__name__)
    app.config.from_object(configs.get(config))

    db.init_app(app)

    register_blueprint(app)

    return app





def register_blueprint(app):
    from .handlers import front, course, admin

    app.register_blueprint(front)
    app.register_blueprint(course)
    app.register_blueprint(admin)

    







