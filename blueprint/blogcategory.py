from flask import Flask,url_for,redirect,render_template,Blueprint,request

from models import Post,db

categories_blog=Blueprint(
    'categories_blog',__name__
)
@categories_blog.route('/blogcategory<int:id>')
def blogcategory(id):
    post=Post.query.filter_by(category_id=id)
    return render_template("pages/blogcategory.html",post=post)

