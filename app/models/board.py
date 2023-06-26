from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    owner= db.Column(db.String(255), nullable=False)
    cards = db.relationship("Card", back_populates="board")
def to_dict(self):
    cards_data = []
    if self.cards:
        for card in self.cards:
            cards_data.append(card.to_dict())

    return ({"board_id": self.board_id,
            "title": self.title,
            "owner": self.owner,
            "cards" : cards_data})

@classmethod 
def from_dict(cls,data_dict):
    return cls(
        title = data_dict["title"],
        owner= data_dict["owner"]
    )
    
