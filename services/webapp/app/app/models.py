from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app.extensions import db
from app.extensions import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

"""
The brand will be the main entity. It will be composed of multiple
hashtags (named keywords because some plateforms don't have hashtags).
An user can create multiple brands and a number of linked keywords.
"""
class Brand(db.Model):

    id        = db.Column(db.Integer,      primary_key=True)
    brandname = db.Column(db.String(120),  unique = True)

    def __init__(self, brandname):
        self.id          = brand
        self.brandname   = brandname

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.brandname)

    def save(self):

        # inject self into db session
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self

class Keyword(db.Model):

    id      = db.Column(db.Integer,      primary_key=True)
    keyword = db.Column(db.String(120),  unique = True)
    active  = db.Column(db.Boolean)

    def __init__(self, keyword, active):
        self.keyword     = keyword
        self.active      = active

    def __repr__(self):
        return str(self.id) + ' - ' + str(self.keyword)

    def save(self):

        # inject self into db session
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self

"""
First we store the raw datas. So we create a JSON storage in the db
It's useful because it will limit the number of request and ensur if we do
evolutions later based on new datas in the api for exemple or new usages we will
already have collected the maximum amount of infos
"""

class RawTweet(db.Model):

    id        = db.Column(db.Integer, primary_key=True)
    rawtweet = db.Column(db.JSON)

    def __init__(self, rawtweet):
        self.rawtweet   = rawtweet

    def __repr__(self):
        return str(self.id) + ' - ' + 'rawtweet'

    def save(self):

        # inject self into db session
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self

class RawGram(db.Model):

    id       = db.Column(db.Integer, primary_key=True)
    rawgram = db.Column(db.JSON)

    def __init__(self, raw_tweet):
        self.rawgram   = rawgram

    def __repr__(self):
        return str(self.id) + ' - ' + 'rawgram'

    def save(self):

        # inject self into db session
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self
