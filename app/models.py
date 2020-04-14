from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from datetime import datetime

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    team = db.Column(db.String(64))
    player = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Player(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    sofifa_id = db.Column(db.Integer, index=True)
    club = db.Column(db.String(64), index=True)
    country = db.Column(db.String(64), index=True)
    short_name = db.Column(db.String(128), index=True, unique=True)
    long_name = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        return '<Player ID: {}, Name: {}>'.format(self.player_id, self.short_name)

class Result(db.Model):
    result_no = db.Column(db.Integer, primary_key=True)
    player1_id = db.Column(db.Integer, index=True)
    player2_id = db.Column(db.Integer,index=True)
    selection = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<{} vs. {}, result:{}>'.format(self.player1_id,self.player2_id,self.selection)

