from app import db


class Board(db.Model):
    __tablename__ = 'board'

    id= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    owner = db.Column(db.String(255))
    cards = db.relationship("Card", back_populates="board")

    def __init__(self,title, owner):
        self.title = title
        self.owner = owner

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "owner": self.owner
        }

    @classmethod
    def from_dict(cls,board_data):
        return cls(
            title=board_data["title"],
            owner=board_data["owner"]
        )

from app.models.board import Board