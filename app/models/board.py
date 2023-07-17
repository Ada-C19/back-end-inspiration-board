from app import db

class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner = db.Column(db.String)
    title = db.Column(db.String)
    cards = db.relationship("Card", back_populates='board',cascade = "all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "owner": self.owner,
            "title": self.title
        }

    @classmethod
    def from_dict(cls, dict_data):
        return Board(owner = dict_data['owner'], title = dict_data['title'])
