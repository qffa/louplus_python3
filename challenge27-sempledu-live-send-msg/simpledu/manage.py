from simpledu.app import create_app




app = create_app('development')


if __name__ == '__main__':
#使用gevent提供的WSGI服务器，并启用WebSocket支持

    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    #创建一个WSGIServer，包含我们的app和gevent的WebSocketHandler
    server = pywsgi.WSGISserver(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()





