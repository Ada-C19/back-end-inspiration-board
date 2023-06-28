from app import db

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    likes = db.Column(db.Integer, default=0)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    board = db.relationship("Board", back_populates='cards')

    def to_dict(self):
        return {
            'id': self.id,
            'message': self.message,
            'likes': self.likes,
            'board': self.board.title,
        }