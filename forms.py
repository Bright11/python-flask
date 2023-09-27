from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField, FileField,TextAreaField

from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    username=StringField('username',validators=[DataRequired(), Length(min=5,max=20)])
    email=StringField("Email",validators=[DataRequired(), Email()])
    password=PasswordField("Password",[DataRequired()])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(), EqualTo("password")])
    image=FileField("Profile Pic")
    submit=SubmitField("Sign Up")
    
    
    
class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(), Email()])
    password=PasswordField('Password',[DataRequired()])
    remember=BooleanField("Remember Me")
    submit=SubmitField("Login")
    
class CategoryForm(FlaskForm):
    name=StringField('Category Name',validators=[DataRequired()])
    submit=SubmitField("save")
    
    
    
class PostForm(FlaskForm):
    title=StringField("Blog Title", validators=[DataRequired()])
    content=TextAreaField("Blog Content",validators=[DataRequired()])
    image=FileField("Blog Image",validators=[DataRequired()])
    submit=SubmitField("save")
    