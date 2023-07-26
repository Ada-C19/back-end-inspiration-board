from app import db
from flask import abort, make_response, jsonify

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)
    cards = db.relationship("Card", back_populates="board")

    @classmethod
    def from_dict(cls, board_data):
        try:
            if board_data["title"] == "":
                raise ValueError

            if board_data["owner"] == "":
                raise ValueError

            new_board = cls(
                title=board_data["title"],
                owner=board_data["owner"]
            )
        except (ValueError, KeyError):
            abort(make_response(jsonify({"details": "Invalid data"}), 400))

        return new_board

    def to_dict(self):
        board_as_dict = {}
        board_as_dict["board_id"]=self.board_id
        board_as_dict["title"]=self.title
        board_as_dict["owner"]=self.owner

        return board_as_dict 