
#��ҳ��ͼ


from flask import render_template
from flask.views import MethodView


class IndexView(MethodView):
    #��ҳ��ͼ


    def get(self):
        #��Ⱦģ��

        return render_template('index.html')


