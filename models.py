from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


def connect_db(app):

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ Pet """

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    photo_url = db.Column(
        db.Text, default='https://thecontemporarypet.com/wp-content/themes/contemporarypet/images/default.png')
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    @validates('name')
    def convert_title(self, key, value):
        return value.title()
