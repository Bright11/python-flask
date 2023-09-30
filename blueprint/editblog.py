from flask import Flask, render_template,Blueprint,redirect,flash,request,url_for,session as newsession
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


editblog_page=Blueprint(
    'editblog_page',__name__,
    static_folder='static',
    template_folder='templates'
)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@editblog_page.route('/editblog/<int:id>',methods=["GET","POST"])
def editblog(id):
    # post=Post.query.get_or_404(id)
    post=Post.query.get_or_404(id)
    cat=Category.query.all()
    blogform=PostForm()
    user=newsession.get("user_id")
    if request.method=="POST":
        # working with slug
        slug=blogform.title.data.lower()
        slug=slug.replace(' ','-')
        slug=unicodedata.normalize('NFKD',slug).encode('ascii','ignore').decode('utf-8')
        slug=re.sub(r'[-]+','-',slug)
        slug=slug.strip('-')
        # # working with image
        # # giving image a unique name
        #upload_file= blogform.image.data
        upload_file=request.files['image']
        
        if upload_file and allowed_file(upload_file.filename):
            # update with image
           
            unique_filename=str(uuid.uuid1())+secure_filename(upload_file.filename)
           
            file_path=os.path.join(app.config['UPLOAD_FOLDER'],unique_filename)
            upload_file.save(file_path)
            post.title=blogform.title.data
            post.content=request.form['content']
            post.category_id=request.form['category_id']
            post.image=unique_filename
            post.slug=slug
            try:
                db.session.commit()
                print("yes blog")
                flash("success")
                return redirect(url_for('editblog_page.editblog', id=id))
                
            except:
                flash("error")
                return redirect(url_for('editblog_page.editblog', id=id))
           
            
        else:
            # update without image
            post.title=blogform.title.data
            post.content=request.form['content']
            post.category_id=request.form['category_id']
            post.slug=slug
            
            try:
                #db.session.add(post)
                print("no image edite")
                db.session.commit()
                flash("Sccess")
                return redirect(url_for('editblog_page.editblog', id=id))
                
            except:
                flash("There was an error")
                return redirect(url_for('editblog_page.editblog', id=id))
            
        
    else:
        blogform.title.data=post.title
        blogform.image.data=post.image
        blogform.content.data=post.content
        return render_template('admin/editblog.html',blogform=blogform,cat=cat,post=post)