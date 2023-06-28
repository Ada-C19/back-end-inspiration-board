from app import db
from datetime import datetime

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)
    theme = db.Column(db.String, nullable=True)
    date_created = db.Column(db.DateTime)
    cards = db.relationship(
        "Card",
        cascade="all, delete",
        back_populates="board"
    )

    def to_dict(self):
        board_dict = {
            "id": self.id,
            "owner": self.owner,
            "title": self.title,
            "description": self.description,
            "theme": self.theme,
            "date_created": self.date_created,
            "cards": [card.to_dict() for card in self.cards]
        }

        return board_dict

    @classmethod
    def from_dict(cls, data):
        return Board(
            owner=data["owner"],
            title=data["title"],
            description=data["description"],
            theme=data.get("theme", None),
            date_created=datetime.now(),
        )

    @classmethod
    def get_required_fields(self):
        return ["owner", "title", "description"]