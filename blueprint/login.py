from flask import Flask,url_for,flash,redirect,Blueprint,request,session
from models import User
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user, login_required, current_user,LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
login_form=Blueprint(
    'login_form',__name__,
)




@login_form.route('/login',methods=['POST'])
def login():
    user=User.query.filter_by(email=request.form['email']).first()
    password=bcrypt.check_password_hash(user.password,request.form['password'])
    if user and password:
        session['username']=user.username
        session['image'] = 'images/' + user.image
        session['email']=user.email,
        session['user_id']=user.id
        return redirect(url_for('home_page.home'))
    else:
        return redirect(url_for('register_page.register'))