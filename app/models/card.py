from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincreme=True)
    message = db.Column(db.String)
    liked_count = db.Column(db.Integer)
