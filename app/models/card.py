from app import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=True)
    board = db.relationship("Board", back_populates="cards")

    def to_dict(self):
        card_dict = dict(
            id=self.id,
            message=self.message,
            likes_count=self.likes_count
        )

        return card_dict