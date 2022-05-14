from flask import render_template,redirect,url_for
from flask_login import login_required,current_user
from . import main
from ..models import Pitch
from .forms import PitchForm

@main.route("/")
def index():
    pitches = Pitch.query.all()
    quotes = Pitch.query.filter_by(category='Quotes').all()
    pickup_lines = Pitch.query.filter_by(category='Pickup_lines').all()
    memes = Pitch.query.filter_by(category='Memes').all()
    
    title = 'Home - Pitch Your Thoughts'
    
    return render_template("index.html", title=title, pitches=pitches, quotes=quotes, pickup_lines=pickup_lines, memes=memes)

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
    return render_template('pitch.html',form=form)
        