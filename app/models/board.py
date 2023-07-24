from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer,  primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)
    cards = db.relationship("Card", back_populates="board", lazy=True)

    def to_dict(self):
        board_as_dict = {}
        board_as_dict["board_id"] = self.board_id
        board_as_dict["title"] = self.title
        board_as_dict["owner"] = self.owner
        return board_as_dict
    
    def get_cards(self):
        board_as_dict_with_cards = self.to_dict()
        cards = [card.to_dict() for card in self.cards]
        board_as_dict_with_cards["cards"] = cards
        return board_as_dict_with_cards
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title = data_dict["title"],
            owner = data_dict["owner"]
        )