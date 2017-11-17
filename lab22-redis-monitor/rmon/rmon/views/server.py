from flask import request, g

from rmon.common.rest import ReswView
from rmon.models import Server, ServerSchema


class ServerList(RestView):
    """获取Redis列表

    """

    def get(self):
        servers = Server.query.all()
        return ServerSchema().dump(servers, many=True).data

    def post(self):
        """创建Redis服务器

        """
        data = request.get_json()
        server, errors = ServerSchema().load(data)

        if errors:
            return error, 400

        server.ping()
        server.save()

        return {'ok': True}, 201
