from flask import render_template,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from ..models import Pitch, User
from .forms import PitchForm, UpdateProfile

@main.route("/")
def index():
    pitches = Pitch.query.all()
    quotes = Pitch.query.filter_by(category='Quotes').all()
    pickup_lines = Pitch.query.filter_by(category='Pickup_lines').all()
    memes = Pitch.query.filter_by(category='Memes').all()
    
    title = 'Home - Pitch Your Thoughts'
    
    return render_template("index.html", title=title, pitches=pitches, quotes=quotes, pickup_lines=pickup_lines, memes=memes)

@main.route("/user/<uname>")
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route("/user/<uname>/update",methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username =uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_user()
        
        return redirect(url_for(".profile",uname=user.username))
    return render_template('profile/update.html', form =form)

@main.route("/pitch/new/<id>", methods=['GET', 'POST'])
@login_required
def add_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        category=form.category.data
        title=form.title.data
        pitch=form.pitch.data
        user_id = current_user
        new_pitch= Pitch(category=category, title=title,pitch=pitch, user=user_id)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))
    title = 'Create New Pitch'
    return render_template('pitch.html', title=title, form=form)
        