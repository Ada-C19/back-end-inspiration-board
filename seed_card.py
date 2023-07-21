from app import create_app, db
from app.models.card import Card
from app.models.board import Board

my_app = create_app()
with my_app.app_context():
    # Get the "reminders" board from the database
    reminders_board = Board.query.filter_by(title="reminders").first()
    capstone_ideas_board = Board.query.filter_by(title="capstone ideas").first()
    quotes_board = Board.query.filter_by(title="quotes").first()
    advice_board = Board.query.filter_by(title="advice").first()
    jokes_board = Board.query.filter_by(title="jokes").first()

    # Create and add cards associated with the "reminders" board
    db.session.add(Card(message="Buy groceries", likes_count=0, board_id=reminders_board.id))
    db.session.add(Card(message="Call Mom", likes_count=0, board_id=reminders_board.id))
    db.session.add(Card(message="Finish homework", likes_count=0, board_id=reminders_board.id))
    db.session.add(Card(message="dont stay up late, it will make you old", likes_count=0, board_id=advice_board.id))
    db.session.add(Card(message="a social media platform called fakebook", likes_count=0, board_id=capstone_ideas_board.id))
    db.session.add(Card(message="I think then I code", likes_count=0,board_id=quotes_board.id))
    db.session.add(Card(message="never leave your keys in the car", likes_count=0, board_id=advice_board.id))
    db.session.add(Card(message="knock knock... nothing I dont know any jokes", likes_count=0, board_id=jokes_board.id))
    db.session.commit()