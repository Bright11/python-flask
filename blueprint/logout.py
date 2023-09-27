from flask import Flask,session,url_for,flash,redirect,Blueprint

# app=Flask(__name__)

logoutuser=Blueprint(
    'logoutuser',__name__
)

@logoutuser.route('/logout')
def logout():
    session.pop('username',None)
    session.pop('image',None)
    session.pop('email',None)
    return redirect(url_for("register_page.register"))