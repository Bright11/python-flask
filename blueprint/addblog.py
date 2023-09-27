from flask import Flask, Blueprint, redirect, render_template,url_for,flash,session,request
from forms import PostForm
from werkzeug.utils import secure_filename
from models import Post,db,Category
import os
import uuid as uuid
import re
import unicodedata

app=Flask(__name__)

UPLOAD_FOLDER='static/blogsimg'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS']={"png","jpg","jpeg"}

addblog_page=Blueprint(
    "addblog_page",__name__,
    static_folder='static',
    template_folder='templates'
)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
        
@addblog_page.route("/addblog",methods=['GET','POST'])
def addblog():
    cat=Category.query.all()
    blogform=PostForm()
    if blogform.validate_on_submit():
        
        user=session['user_id'],
        # slug
        slug=blogform.title.data.lower()
        slug=slug.replace(' ','-')
        slug = unicodedata.normalize('NFKD', slug).encode('ascii', 'ignore').decode('utf-8')
        slug=re.sub(r'[-]+', '-', slug)
        slug=slug.strip('-')
        # 
        uploaded_file=blogform.image.data
        if uploaded_file and allowed_file(uploaded_file.filename):
            unique_filename=str(uuid.uuid4())+ secure_filename(uploaded_file.filename)
            file_path=os.path.join(app.config['UPLOAD_FOLDER'],unique_filename)
            uploaded_file.save(file_path)
            newpost=Post(
            title=blogform.title.data,
            content=blogform.content.data,
            image=unique_filename,
            user_id=user,
            category_id=request.form.get('category_id'),
            slug=slug,
            
            )
            db.session.add(newpost)
            db.session.commit()
            flash("Blog created")
            return redirect(url_for('addblog_page.addblog'))
            
        else:
            pass
        pass
    else:
        return render_template("admin/addblog.html",blogform=blogform,cat=cat)
    
    
   
