from flask import Flask, render_template,url_for,flash,redirect
from models import db,Category,Post,User
from blueprint.about import about_page
from blueprint.home import home_page
from blueprint.register import register_page
from blueprint.login import login_form
from blueprint.logout import logoutuser
from blueprint.category import category_page
from blueprint.addblog import addblog_page
from blueprint.editblog import editblog_page
from blueprint.editcat import editcategroy
from blueprint.blogcategory import categories_blog
from blueprint.blogdetails import blogdetails_page

# 


app=Flask(__name__)
app.register_blueprint(about_page)
app.register_blueprint(home_page)
app.register_blueprint(register_page)
app.register_blueprint(login_form)
app.register_blueprint(logoutuser)
app.register_blueprint(category_page)
app.register_blueprint(addblog_page)
app.register_blueprint(editblog_page)
app.register_blueprint(editcategroy)
app.register_blueprint(categories_blog)
app.register_blueprint(blogdetails_page)


app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blogdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# @app.before_first_request
# def create_table():
#     db.create_all()

with app.app_context():
    db.create_all()

@app.context_processor
def inject_global_data():
    # You can add any data you want to make available to all templates
    categorydata=Category.query.all()
    categorycount=Category.query.count()
    users=User.query.count()
    blog=Post.query.count()
    return {'categorydata': categorydata,'categorycount':categorycount,"users":users,'blog':blog}

# https://bunq-templatesyard.blogspot.com/


# the end

# setting up routes




if __name__ == '__main__':
    app.run(debug=True)