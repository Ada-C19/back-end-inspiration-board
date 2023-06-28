from app import db
from datetime import datetime

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)
    date_created = db.Column(db.DateTime)
    board = db.relationship("Board", back_populates="cards")
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))

    def to_dict(self):
        card_dict = {
            "id": self.id,
            "message": self.message,
            "likes_count": self.likes_count,
            "date_created": self.date_created,
            "board_id": self.board_id,
        }
        return card_dict

    @classmethod
    def from_dict(cls, data):
        return Card(
            message=data["message"],
            likes_count=0,
            date_created=datetime.now(),
            board_id=data["board_id"],
        )

    @classmethod
    def get_required_fields(self):
        return ["message", "likes_count", "board_id"]