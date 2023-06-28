from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(40), nullable=False )
    likes_count = db.Column(db.Integer, nullable=True)
    board_id = db.Column(db.Integer, db.ForeignKey("board.board_id"))
    board = db.relationship("Board", back_populates="cards")

    def to_dict_cards(self):
        return {
            "card_id": self.card_id,
            "board_id": self.board_id,
            "message": self.message,
            "likes_count": 0 if self.likes_count == None else self.likes_count
        }
