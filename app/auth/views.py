from flask import render_template
from . import auth

@auth.route("/login")
def login():
    title = 'Login'
    
    return render_template("auth/login.html", title=title)