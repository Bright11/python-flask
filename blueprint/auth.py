from functools import wraps

from flask import session,request,redirect,url_for

def login_required(func):
    @wraps(func)
    def decorated_function(*args,**kwargs):
        if not session.get("user"):
            return redirect(url_for("register_page.register"))
        return func(*args,**kwargs)
    return decorated_function