""" rmon.views.urls

����������APT��Ӧ��URL

"""


from flask import Blueprint

api = Blueprint('api', __name__)

api.add_url_rule('/', view_func=IndexView.as_view('index'))
