from app import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)

    @classmethod
    def from_dict(cls, board_data):
        return Board(
            title=board_data["title"],
            owner=board_data["owner"]
        )