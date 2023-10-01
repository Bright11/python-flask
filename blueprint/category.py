from flask import Flask,url_for,redirect,flash,Blueprint,render_template,request
from forms import CategoryForm
from models import Category,db
# secure pages
from blueprint.auth import login_required

category_page=Blueprint(
    'category_page',__name__
)

@category_page.route('/category',methods=['GET','POST'])
@login_required
def category():
    catform=CategoryForm()
    if catform.validate_on_submit():
        checkcat=Category.query.filter_by(name=catform.name.data).first()
        if checkcat:
            flash(f'Category name already exist {catform.name.data}','error')
            return redirect(url_for('category_page.category'))
        else:
           
            category=Category(name=catform.name.data)
            db.session.add(category)
            db.session.commit()
            flash(f'Category {catform.name.data} added','success')
            return redirect(url_for('category_page.category'))
    else:
        category=Category.query.all()
        return render_template('admin/category.html',catform=catform,category=category)