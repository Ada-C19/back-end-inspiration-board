from app import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    cards = db.relationship("Card", back_populates="board")


    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            owner=self.owner,
        )


    @classmethod
    def from_dict(cls, board_data):
        return Board(
            title=board_data["title"],
            owner=board_data["owner"],
            # does this cards section need to be conditional for if there are no cards? 
            # does cards start at 0 or will this result in a KeyError? 
            # cards=board_data["cards"],
        )