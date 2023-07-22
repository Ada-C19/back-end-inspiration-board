from app import db
from flask import make_response, abort

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    board = db.relationship("Board", back_populates="cards")

    def to_dict(self):
        card_dict = dict(
            id=self.id,
            message=self.message,
            likes_count=self.likes_count
        )

        return card_dict

    # including from_dict helper function in case it is needed
    # for user input
    @classmethod
    def from_dict(cls, data_dict):
        try:
            new_instance = cls(message=data_dict["message"], likes_count=0)
        except KeyError: 
            abort(make_response({"details": "Invalid data"}, 400))

        return new_instance