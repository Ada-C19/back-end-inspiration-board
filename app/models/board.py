from app import db


class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)
    cards = db.relationship("Card", back_populates="board")


    def to_dict(self):
        board_as_dict = {}
        board_as_dict_as_dict["id"] = self.id
        board_as_dict["title"] = self.title
        board_as_dict["owner"] = self.owner
        board_as_dict["cards"] = self.cards
        return book_as_dict
