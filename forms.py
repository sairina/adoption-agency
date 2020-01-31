from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, ValidationError, url


def validate_age(form, field):
    """ Acceptable age """

    if field.data > 30 or field.data < 0:
        raise ValidationError('Age must be between 0-30')


class AddPetForm(FlaskForm):
    """ Form for adding pets """

    name = StringField("Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[
                          ('dog', 'Dog'), ('cat', 'Cat'),
                          ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), url()])
    age = FloatField("Age", validators=[InputRequired(), validate_age])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """ Form for editing pets """

    photo_url = StringField("Photo URL", validators=[Optional(), url()])
    notes = StringField("Notes")
    available = BooleanField('Available for Adoption?')
