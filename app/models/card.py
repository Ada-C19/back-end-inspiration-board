from app import db


class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String, nullable=False)
    likes_count = db.Column(db.Integer, nullable=True)
    board_id = db.Column(db.Integer, db.ForeignKey("board.board_id"))
    board = db.relationship("Board", back_populates="cards")

    @classmethod
    def from_dict_cards(cls, card_data):
        new_card = Card(
            message=card_data["message"]
        )

        return new_card

    def to_dict_cards(self):
        return {
            "id": self.card_id,
            "board_id": self.board_id,
            "message": self.message,
            "likes_count": self.likes_count
        }


