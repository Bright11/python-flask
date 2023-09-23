from flask import Flask, Blueprint, render_template,url_for,flash,redirect

home_page=Blueprint(
    'home_page',__name__,static_folder='static',template_folder='templates'
)


@home_page.route("/")
@home_page.route("/home")
def home():
    return render_template('pages/home.html')
