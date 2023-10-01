from flask import Flask, url_for,redirect,Blueprint,request,render_template

from forms import CategoryForm
from models import Category,db
# secure pages
from blueprint.auth import login_required

editcategroy=Blueprint(
    'editcategroy',__name__ 
)

@editcategroy.route('/editcat<int:id>',methods=['GET','POST'])
@login_required
def editcat(id):
    #cat=db.session.query(Category).filter_by(id=id).first()
    cat=Category.query.get_or_404(id)
    catform=CategoryForm()
    if request.method=="POST" and catform.validate_on_submit():
        cat.name=catform.name.data
        print("new name",catform.name.data)
        
        try:
            #db.session.add(cat)
            db.session.commit()
            print("success")
            return redirect(url_for('category_page.category'))
            
        except:
            return redirect(url_for('category_page.category'))
        
    catform.name.data=cat.name
    return render_template("admin/editcat.html",cat=cat,catform=catform)
    pass