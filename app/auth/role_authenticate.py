from functools import wraps
from flask import abort
from flask_login import current_user
from app.auth.roles import Roles


def role_authenticate(roles: list):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.is_authenticated:
                if current_user.role in roles:
                    return f(*args, **kwargs)
                abort(403)
            abort(401)
        return decorated_function
    return decorator
