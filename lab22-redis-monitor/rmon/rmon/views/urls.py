""" rmon.views.urls

定义了所有APT对应的URL

"""

from flask import Blueprint
from rmon.views.index import IndexView


api = Blueprint('api', __name__)

api.add_url_rule('/', view_func=IndexView.as_view('index'))
