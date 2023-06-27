from app import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)
    board_id = db.Column(db.ForeignKey('board.id'))
    board = db.relationship("Board", back_populates="cards")
