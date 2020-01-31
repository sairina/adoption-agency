from flask import Flask, redirect, render_template, request
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "poiawhefiusiuawe"
debug = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    """ Homepage of Pets List """

    return render_template("index.html", pets=Pet.query.all())


@app.route("/add", methods=["GET", "POST"])
def create_pet_form():
    """ Form for adding pets """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url = form.photo_url.data or None
        notes = form.notes.data or None

        pet = Pet(name=name, species=species, age=age,
                  photo_url=photo_url, notes=notes)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("add-form.html", form=form)
