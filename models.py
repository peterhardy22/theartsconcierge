import csv
import json
import yaml
from app import db


def csv_importer():
    with open('static/data/csv/bayareatracker.csv') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        first_line = True
        exhibits = []
        for row in csv_data:
            if not first_line:
                exhibits.append({
                    "institution": row[0],
                    "title": row[1],
                    "dates": row[2],
                    "image": row[3],
                    "link": row[4]
                })
            else:
                first_line = False

    exhibits_json = json.dumps(exhibits)

    return yaml.safe_load(exhibits_json)


class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "{}".format(self.name)


class Artwork(db.Model):
    __tablename__ = "artworks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    medium = db.Column(db.String)
    dimensions = db.Column(db.String)
    image = db.Column(db.String)
    location = db.Column(db.String)
    city = db.Column(db.String)
    country = db.Column(db.String)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    on_view = db.Column(db.Boolean, default=False)

    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    artist = db.relationship("Artist", backref=db.backref(
        "artworks", order_by=id))
