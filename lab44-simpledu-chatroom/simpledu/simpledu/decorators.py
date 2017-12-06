from flask import abort
from flask_login import current_user
from functools import wraps
from simpledu.models import User






def role_required(role):
    """带参数装饰器，可以用它保护一个路由处理函数只能被特定的角色访问：
        @role_required(User.ADMIN）
        def admin():
            pass

    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            #未登录用户或者角色不满足引发404
            #为什么不是403？因为不希望把路由暴露给不具权限的用户

            if not current_user.is_authenticated or current_user.role < role:
                abort(404)

            return func(*args, **kwargs)
        
        return wrapper

    return decorator





#特定角色装饰器
staff_required = role_required(User.ROLE_STAFF)
admin_required = role_required(User.ROLE_ADMIN)




