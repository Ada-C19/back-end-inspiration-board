from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)
    # card = db.relationship("Card", back_populates="boards")
    # card_id = db.Column(db.Integer, db.ForeignKey("card.id"))
