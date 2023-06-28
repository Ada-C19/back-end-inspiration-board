from app import db


class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String, nullable=False)
    likes_count = db.Column(db.Integer, nullable=False)
    board = db.relationship("Board", back_populates="cards", lazy=True)
    board_id = db.Column(db.Integer, db.ForeignKey(
        "board.board_id", ), nullable=True)
        
    # def to_dict(self):
    #     card_as_dict = {}
    #     card_as_dict["id"] = self.card_id
    #     card_as_dict["message"] = self.message
    #     card_as_dict["likes_count"] = self.likes_count
    #     return card_as_dict


    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "likes_count": self.likes_count
        }
