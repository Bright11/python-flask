from flask import Flask,Blueprint, redirect,render_template,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm
import uuid as uuid
from werkzeug.utils import secure_filename
import os
from models import User,db
from flask_bcrypt import Bcrypt

 
 
app=Flask(__name__)
# upload images
UPLOAD_FOLDER='static/images/'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS']={'png','jpg','jpeg'}
bcrypt = Bcrypt(app)
register_page=Blueprint(
    "register_page",__name__, static_folder='static',
    template_folder='templates'
)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@register_page.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
            check_email=User.query.filter_by(email=form.email.data).first()
            if check_email:
                flash("user already exists")
                return redirect(url_for('register_page.register'))
            else:
                #print("yes face 1")
                uploaded_file = form.image.data
                if uploaded_file and allowed_file(uploaded_file.filename):
                    print("yes 22")
                    unique_filename = str(uuid.uuid4()) + secure_filename(uploaded_file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                    uploaded_file.save(file_path)  # Use uploaded_file.save, not file_path.save
                    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                    new_user = User(
                    username=form.username.data,
                    email=form.email.data,
                    password=hashed_password,
                    image=unique_filename  # Assuming you have a 'profile_image' field in your User model
                )
                    db.session.add(new_user)
                    db.session.commit()
                    flash(f'Account created successfully! Username: {form.username.data}', 'success')
                    return redirect(url_for('register_page.register'))
                
                else:
                    return redirect(url_for('register_page.register'))


    return render_template('pages/register.html', title='Registration page', form=form)
