from flask import Flask, render_template,url_for,flash,redirect
from models import db,User, Post
from blueprint.about import about_page
from blueprint.home import home_page
from blueprint.register import register_page
from blueprint.login import login_form
from blueprint.logout import logoutuser
from blueprint.category import category_page
from blueprint.addblog import addblog_page
# 
app=Flask(__name__)
app.register_blueprint(about_page)
app.register_blueprint(home_page)
app.register_blueprint(register_page)
app.register_blueprint(login_form)
app.register_blueprint(logoutuser)
app.register_blueprint(category_page)
app.register_blueprint(addblog_page)
app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blogdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# @app.before_first_request
# def create_table():
#     db.create_all()

with app.app_context():
    db.create_all()



# https://bunq-templatesyard.blogspot.com/


# the end

# setting up routes




if __name__ == '__main__':
    app.run(debug=True)