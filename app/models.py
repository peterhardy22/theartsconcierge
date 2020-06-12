from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from app import db, login
import csv
import json
import yaml


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(140))
    artwork = db.Column(db.String(140))
    medium = db.Column(db.String(140))
    location = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


def csv_importer():
    with open('app/static/data/csv/bayareatracker.csv') as csv_file:
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
