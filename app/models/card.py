from app import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(40), nullable=False)
    likes_count = db.Column(db.Integer)
    color = db.Column(db.String, default=0)
    board_id = db.Column(db.Integer, db.ForeignKey("board.id"))
    board = db.relationship("Board", back_populates = "card")