from flask import render_template,redirect,url_for,flash,request
from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import User
from flask_login import login_required, login_user, logout_user
from ..email import mail_message

@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
    flash('Invalid username or Password')
    title = "User Login"
    return render_template('auth/login.html', form=form, title=title)

@auth.route('/signup',methods = ['GET','POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username = form.username.data,password=form.password.data)
        user.save_user()
        mail_message("Welcome to Pitcher","email/welcome_user", user.email,user=user)
        return redirect(url_for('auth.login'))
    title = 'Sign Up'
    return render_template('auth/signup.html',title=title, reg_form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))