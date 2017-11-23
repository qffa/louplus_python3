import re
import os
from wechatpy.messages import TextMessage
from wechatpy import create_reply
from qqwry import QQwry



class CommandHandler:
    command = ''

    def check_match(self, message):
        """检查消息是否匹配命令模式

        """
        if not isinstance(message, TextMessage):
            return False

        if not message.contnet.strip().lower().startwith(self.command):
            return False

        return True



class IPLocationHandler(CommandHandler):
    def handle(self, message):
        ip = re.search('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', message.content).group(0)

        q = QQwry()
        q.load_file('qqwry.dat')

        content = q.lookup(ip)

        reply = create_reply(content, message)





        return reply
