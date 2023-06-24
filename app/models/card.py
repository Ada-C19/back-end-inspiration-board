from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)
    likes_count = db.Column(db.Integer, default=0)
    board = db.relationship("Board", back_populates = "cards")
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'))


    def to_dict(self):
        card_dict={
            "id":self.card_id,
            "message":self.message,
            "likes_count":self.likes_count
        }
        return card_dict

    @classmethod
    def from_dict(cls, data_dict):
        new_obj = cls(
            message = data_dict["message"],
            board_id = data_dict["board_id"]
        )
        return new_obj