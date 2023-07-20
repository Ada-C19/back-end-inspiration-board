from app import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer, default=0)
    board_id = db.Column(db.ForeignKey("board.id"))
    board = db.relationship("Board", back_populates="cards")

    @classmethod 
    def dict_to_model(cls, data_dict):
        return cls(message = data_dict["message"], likes_count=data_dict["likes_count"])
    
    def make_card_dict(self):
        return dict(
            id=self.id,
            message=self.message,
            likes_count=self.likes_count,
            board_id=self.board_id,
        )


