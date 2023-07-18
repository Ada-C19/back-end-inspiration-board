from app import db


class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(40), nullable=False)
    likes_count = db.Column(db.Integer, default=0)
    board = db.relationship("Board", back_populates="cards", lazy=True)
    board_id = db.Column(db.Integer, db.ForeignKey(
        "board.board_id", ), nullable=True)

    def to_dict(self):
        return {
            "card_id": self.card_id,
            "message": self.message,
            "likes_count": self.likes_count,
            "board_id": self.board_id
        }

    @classmethod
    def from_dict(cls, request_data):
        new_board = cls(
            message=request_data["message"],
            likes_count=0
        )

        return new_board
