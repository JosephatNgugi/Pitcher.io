from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,TextAreaField,SubmitField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
    category = SelectField(u'Category', choices=[('Quotes','Quotes'), ('Pickup Lines', 'Pickup Lines'), ('Memes', 'Memes')], validators=[InputRequired()])
    title = StringField("Pitch Title(Optional)")
    pitch = TextAreaField('Share Your Pitch', validators=[InputRequired()])
    submit = SubmitField('Post')
    
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators=[InputRequired()])
    submit = SubmitField('Save')