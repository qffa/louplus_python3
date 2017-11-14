""" rmon.views.urls

定义了所有APT对应的URL

"""


from flask import Blueprint

api = Blueprint('api', __name__)

api.add_url_rule('/', view_func=IndexView.as_view('index'))
