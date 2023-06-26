from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)
    cards = db.relationship("Card", back_populates="board")
    
@classmethod
def board_from_dict(cls, board_data):
    new_board = Board(title=board_data["title"])
    return new_board

def board_to_dict(self):
    board_as_dict = {}

    board_as_dict["id"] = self.board_id
    board_as_dict["title"] = self.title
    board_as_dict["owner"] = self.owner
    
    # code here for cards

    return board_as_dict

