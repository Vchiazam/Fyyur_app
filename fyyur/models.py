from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False)
    city = db.Column(db.String(120),nullable=False)
    state = db.Column(db.String(120),nullable=False)
    address = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.String(120),nullable=True)
    image_link = db.Column(db.String(500),nullable=True)
    facebook_link = db.Column(db.String(500),nullable=True)
    website_link = db.Column(db.String(500),nullable=True)
    description = db.Column(db.String(),nullable=True)
    looking_for_talent = db.Column(db.Boolean, nullable=False, default=False)
    genres =  db.Column(db.String(120),nullable=True)
    shows = db.relationship("Shows",  backref="Venue", lazy=True)


    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable=False)
    city = db.Column(db.String(120),nullable=False)
    state = db.Column(db.String(120),nullable=False)
    phone = db.Column(db.String(120),nullable=True)
    image_link = db.Column(db.String(500),nullable=True)
    facebook_link = db.Column(db.String(500),nullable=True)
    website_link = db.Column(db.String(500),nullable=True)
    description = db.Column(db.String(),nullable=True)
    looking_for_venues = db.Column(db.Boolean, nullable=False, default=False)
    genres =  db.Column(db.String(120),nullable=True)
    shows = db.relationship("Shows", backref="Artist", lazy=True)

class Shows(db.Model):
   __tablename__ = 'Shows'
   id = db.Column(db.Integer, primary_key=True)
   start_time = db.Column(db.DateTime,nullable=False)
   artist_id =  db.Column(db.Integer, db.ForeignKey('Artist.id'),nullable = False)
   venue_id =  db.Column(db.Integer, db.ForeignKey('Venue.id'),nullable = False)