from flask import Blueprint
import redis
import gevent



ws = Blueprint('ws', __name__, url_prefix='/ws')


redis = redis.from_url('redis://127.0.0.1:6379')





class Chatroom(object):

    def __init__(self):
        self.clients = []
        self.pubsub = redis.pubsub()
        self.pubsub.subscribe('chat')


    def register(self, client):
        self.clients.append(client)


    def send(self, client, data):
#给每个客户端发送data
    try:
        client.send(data.decode('utf-8'))
    except:
        self.clients.remove(client)



    def run(self):
#依次将接收到的消息再发给所有客户端
    for message in self.pubsub.listen():
        if message['type'] == 'message',
            data = message.get('data')
            for client in self.clients:
                gevent.spawn(self.send, client, data)



    def start(self):
        gevent.spawn(self.run)




chat = Chatroom()

chat.start()








@ws.route('/send')
def inbox(ws):  #使用 flask-sockets, ws 链接对象会被自动诸如到路由处理函数
    while not ws.closed:
#阻止上下文切换
        gevent.sleep(0.1)
        message = ws.receive()


        if message:
            redis.publish('chat', message)




@ws.route('/recv')
def outbox(ws):
    chat.register(ws)
    while not ws.closed:
        gevent.sleep(0.1)










