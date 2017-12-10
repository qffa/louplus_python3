from flask import Blueprint, render_template, url_for, redirect
from simpledu.decorators import admin_required
from simpledu.forms import MsgForm
import redis
import json



live = Blueprint('live', __name__, url_prefix='/live')



@live.route('/')
def index():
    return render_template('live/index.html')


@live.route('/systemmessage', methods=['POST'])
@admin_required
def send_msg():
    r = redis.from_url('redis://127.0.0.1:6379')
    form = MsgForm()
    if form.validate_on_submit():
        message_text = form.message.data
        message = {'username': 'System', 'text': message_text}
        message = json.dumps(message)
        r.publish('chat', message)
        return redirect(url_for('admin.send_msg'))
    return redirect(url_for('admin.send_msg'))


