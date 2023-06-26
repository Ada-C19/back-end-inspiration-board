from app import db

class Board(db.Model):
    board_id = db.Column(db.integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)
    cards = db.relationship("Card", back_populates="board")

    @classmethod
    def from_dict(cls, board_data):
        new_board = cls(
            title = board_data.get("title"), 
            owner = board_data.get("owner")
        )
        return new_board

    def to_dict(self):
        board_dict = {
            "id": self.board_id,
            "title": self.title,
            "owner": self.owner
        }
        return board_dict
