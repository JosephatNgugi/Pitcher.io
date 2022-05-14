from flask import render_template,redirect,url_for,flash,request
from . import auth
from .forms import LoginForm
from ..models import User
from flask_login import login_user

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