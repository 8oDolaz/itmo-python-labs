import config

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True, default=config.default_note_title)
    text = db.Column(db.Text, nullable=False)

    tag = db.relationship('Tag', backref='tag')

    def __init__(self, title, text, tag):
        self.text = text
        self.title = title
        self.tag = tag


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Integer, nullable=False)

    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))

    def __init__(self, text):
        self.text = text
