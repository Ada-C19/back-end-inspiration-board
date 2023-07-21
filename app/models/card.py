from app import db


class Card(db.Model):
    __tablename__ = 'card'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255))
    likes_count = db.Column(db.Integer)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    board = db.relationship("Board", back_populates="cards")

    def __init__(self, message, likes_count, board_id):
        self.message = message
        self.likes_count = likes_count
        self.board_id = board_id

    def to_json(self):
        return {
            'id': self.id,
            'message': self.message,
            'likes_count': self.likes_count
        }

from app.models.card import Card

