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
        # what about cards?
        # how could we create a list that holds dictionary rep of all of our cards list?
        # look at tasks/goal in task list
        # look into this more ;D calling all cards when we call a board vs calling cards separately
        return board_as_dict
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title = data_dict["title"],
            owner = data_dict["owner"]
        )