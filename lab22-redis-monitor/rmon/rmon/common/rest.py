""" rmon.common.rest

"""


class RestException(Exception):
    """ 异常基类

    """


    def __init__(self, code, message):
        """初始化异常

        Aargs:
            code (int): http status code
            message (str): error message

        """

        self.code = code
        self.message = message
        super(RestException, self).__init__()
