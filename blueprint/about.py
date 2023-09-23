
from flask import Flask, Blueprint, render_template,url_for,flash,redirect

about_page=Blueprint(
    'about_page',__name__, static_folder='static',template_folder='templates'
)
# about us
@about_page.route("/about")
def about():
    
    return render_template("pages/about.html")

# 