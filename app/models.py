from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search = db.Column(db.String(120), index=True)
    source = db.Column(db.String(120), index=True)
    title = db.Column(db.String(120), index=True)
    company = db.Column(db.String(64), index=True)
    age_of_post = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    url = db.Column(db.String(1024))
    time_scrapped = db.Column(db.DateTime, index=True)
    status = db.Column(db.Integer)

    def __repr__(self):
        return '<Job Posting (Title - {}, URL - {}>'.format(self.title, self.url)
