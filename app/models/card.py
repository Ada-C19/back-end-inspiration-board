from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autouncrement=True)
    message = db.Column(db.String(225), nullable=False)
    likes_count= db.Column(db.Integer, nullable=False )

def to_dict(self):
    return ({"card_id": self.card_id,
             "message": self.message,
             "likes_count": self.likes_count})

@classmethod
def from_dict(cls,data_dict):
    return cls(
        messge = data_dict["message"],
        likes_count= data_dict["likes_count"]
    )
