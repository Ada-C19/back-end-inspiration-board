from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    liked_count = db.Column(db.Integer)
    board = db.relationship("Board", back_populates="cards")
    board_fk = db.Column(db.Integer, db.ForeignKey('board.board_id'))


    @classmethod
    def from_dict(cls, card_data):
        new_card = Card(
            message = card_data["message"],
            liked_count = card_data["liked_count"]
        )

        return new_card


    def to_dict(self):
        return {
            "card_id": self.card_id,
            "message": self.message,
            "liked_count": self.liked_count
        }