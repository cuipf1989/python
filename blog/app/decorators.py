# !/usr/bin/python
# coding=utf-8

from functools import wraps
from flask import abort
from flask_login import current_user

'''
def connect_required(permission):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return func(*args, **kwargs)
        return decorated_function
    return decorator
'''

'''
def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)

'''