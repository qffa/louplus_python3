import os
from flask import Flask
import json

def create_app():
    """创建并初始化 Flask app

    Returns:
        app(object): Flask App 实例

    """

    app = Flask('rmon')
    file = os.environ.get('RMON_CONFIG')

    jsonstring = ''

    with open(file, 'r') as f:
        for line in f.readlines():
            if line.strip() != '':
                if line.strip()[0] != '#':
                    jsonstring += line

    config = {}

    for key, value in json.loads(jsonstring).items():
        config[key.upper()] = value


    app.config.update(config)

    print(app.config)

    return app



if __name__ == '__main__':
    create_app()




