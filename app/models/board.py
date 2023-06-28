from app import db
class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)
    cards = db.relationship("Card",back_populates="board")


    @classmethod
    def from_dict_boards(cls, board_data):
        new_board = Board(
            title = board_data["title"],
            owner = board_data["owner"]
        )

        return new_board

    def to_dict_boards(self):
        return {
            "board_id": self.board_id,
            "title": self.title,
            "owner": self.owner
        }