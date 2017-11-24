import re
import os
from wechatpy.messages import TextMessage
from wechatpy import create_reply
from qqwry import QQwry



class CommandHandler:
    command = 'ip'

    def check_match(self, message):
        """检查消息是否匹配命令模式

        """
#        if not isinstance(message, TextMessage):
#           return False

        if not message.content.strip().lower().startswith(self.command):
            return False

        return True



class IPLocationHandler(CommandHandler):

    def handle(self, message):
        if not self.check_match(message):
            return

        ip = re.search('\s\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$', message.content)
        print(ip)

        if ip is None:
            return create_reply('IP地址无效', message)

        q = QQwry()
        q.load_file('qqwry.dat')

        content = q.lookup(ip.group(0))

        reply = create_reply(content[0], message)


        return reply.render()


if __name__ == "__main__":

    class Message():
        content = ''

    message  = Message()
    message.content = 'ip 8.8.8.8.8'

    ip_locater = IPLocationHandler()
    print(message.content)
    content = ip_locater.handle(message)
    
    print(content)
