from rmon.models import Server
from rmon.common.rest import RestException

class TestServer:
    """测试Server相关功能

    """

    def test_save(self, db):
        """测试Server.save保存服务器方法

        """

        assert Server.query.count() == 0
        server = Server(name='test',host='127.0.0.1')
        server.save()

        assert Server.query.count() == 1
        assert server.query.first() == server

    def test_delete(self, db, server):
        """测试Server.delete删除服务器方法

        """
        assert Server.query.count() == 1
        server.delete()

        assert Server.query.count() == 0


    def test_ping_sucess(self, db, server):
        """测试Server.ping方法执行成功

        需要保证Redis服务器监听在127.0.01:6379地址

        """


        assert server.ping() is True


    def test_ping_failed(self, db):
        """测试Server.ping方法执行失败

        Server.ping 方法执行失败时，抛出RestException异常

        """

        server = Server(name='test', host='127.0.0.1', port=6399)

        try:
            server.ping()
        except RestException as e:
            assert e.code == 400
            assert e.message == 'redis server %s can not connected' %server.host
