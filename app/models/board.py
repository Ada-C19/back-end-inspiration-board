from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    owner= db.Column(db.String(255), nullable=False)

def to_dict(self):
    return ({"board_id": self.board_id,
            "title": self.title,
            "owner": self.owner})

@classmethod 
def from_dict(cls,data_dict):
    return cls(
        title = data_dict["title"],
        owner= data_dict["owner"]
    )