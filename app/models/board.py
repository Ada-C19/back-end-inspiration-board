from app import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)

    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, data):
        return Board(
        )