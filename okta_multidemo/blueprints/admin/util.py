from functools import wraps

from flask import current_app, Response, session, request, redirect, url_for


def auth_admin():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_app.blueprints['okta-admin'].token:
                resp = redirect(url_for('okta-admin.login'))
                return resp
            return f(*args, **kwargs)
        return decorated_function
    return decorator
