from flask import render_template

from app.models import Pitch
from . import main

@main.route("/")
def index():
    pitches = Pitch.query.all()
    quotes = Pitch.query.filter_by(category='Quotes').all()
    pickup_lines = Pitch.query.filter_by(category='Pickup_lines').all()
    memes = Pitch.query.filter_by(category='Memes').all()
    
    title = 'Home - Pitch Your Thoughts'
    
    return render_template("index.html", title=title, pitches=pitches, quotes=quotes, pickup_lines=pickup_lines, memes=memes)