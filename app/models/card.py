from app import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)

    def to_dict(self):
        card_dict = {

        }
        return card_dict
    
    @classmethod
    def from_dict(cls, data):
        return Card(
        )