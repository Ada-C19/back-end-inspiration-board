from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)
    cards = db.relationship("Card", back_populates = "board", lazy = True)



    def to_dict(self):
        boards_dict = {
        "id": self.board_id,
        "title": self.title,
        "owner": self.owner,

        }

        if self.card_id:
            boards_dict["card_id"] = self.card_id
        return boards_dict


    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title = data_dict["title"],
            owner = data_dict["owner"]
        )
