from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, ValidationError, url


def validate_species(form, field):
    """ Acceptable species """

    valid_species = ['dog', 'cat', 'porcupine']

    if field.data.lower() not in valid_species:
        raise ValidationError('Species must be valid')


def validate_age(form, field):
    """ Acceptable age """

    if field.data > 30 or field.data < 0:
        raise ValidationError('Age must be between 0-30')


class AddPetForm(FlaskForm):
    """ Form for adding pets """

    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[
                          InputRequired(), validate_species])
    photo_url = StringField("Photo URL", validators=[Optional(), url()])
    age = FloatField("Age", validators=[InputRequired(), validate_age])
    notes = StringField("Notes")
    # available = BooleanField('Available for Adoption?')
