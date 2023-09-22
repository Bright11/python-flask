from datetime import datetime
from flask import Flask, render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy


# 
app=Flask(__name__)
app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)