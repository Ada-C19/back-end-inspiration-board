from app import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)
    theme = db.Column(db.String, nullable=True)
    date_created = db.Column(db.DateTime, nullable=True)
    cards = db.relationship("Card", back_populates="board")

    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, data):
        return Board(
        )