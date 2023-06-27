from app import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)
    board_id = db.Column(db.Integer, db.ForeignKey("board.id"))
    board = db.relationship("Board", back_populates="cards")

    def card_to_dict(self):
        card_as_dict = {}
        card_as_dict["id"] = self.id
        card_as_dict["message"] = self.message
        card_as_dict["likes_count"] = self.likes_count

        return card_as_dict

    @classmethod
    def card_from_dict(cls, card_data):
        new_card = cls(message=card_data["message"],
                       likes_count=card_data.get("likes_count", 0))

        return new_card
