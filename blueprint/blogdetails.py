from flask import Flask,url_for,render_template,redirect,Blueprint,request,session as newsession

from models import Post,db,Comment


blogdetails_page=Blueprint(
    'blogdetails_page',__name__,
    static_folder='static',
    template_folder='templates'
)

@blogdetails_page.route('/blogdetails<string:slug>',methods=['GET','POST'])
def blogdetails(slug):
    blog=Post.query.filter_by(slug=slug).first()
    related_posts = Post.query.filter_by(category_id=blog.category_id).limit(4).all()
    comment=Comment.query.filter_by(post_id=blog.id).all()
    print("slug",slug)
    if request.method=="POST":
        if  newsession.get("user"):
            newcomment=Comment(
            user_id= newsession.get('user_id'),
            comment=request.form['comment'],
             post_id=blog.id
            )
            db.session.add(newcomment)
            db.session.commit()
            return redirect(url_for('blogdetails_page.blogdetails', slug=slug))
        else:
            return redirect(url_for("register_page.register"))
       
    else:
        return render_template("pages/blogdetails.html",blog=blog,related_posts=related_posts,comment=comment)
    
   
        
    
    

    