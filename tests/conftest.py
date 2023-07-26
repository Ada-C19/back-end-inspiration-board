import pytest
from app import create_app
from flask.signals import request_finished
from app import db
from app.models.board import Board
from app.models.card import Card

@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_board(app):
    new_board = Board(board_id=1, title="Life Goals", owner="Angie")
    db.session.add(new_board)
    db.session.commit()
    return new_board

@pytest.fixture
def three_boards(app):
    db.session.add_all([
        Board(board_id=1, title="Life Goals", owner="Angie"),
        Board(board_id=2, title="Dream Wedding", owner="Danica"),
        Board(board_id=3, title="Self-Improvement", owner="Alejandra")
    ])
    db.session.commit()

@pytest.fixture
def one_card(app):
    new_board = Board(board_id=1, title="Life Goals", owner="Angie")
    new_card = Card(board_id=1, card_id=1, likes_count=0, message="Good things are coming!")
    new_board.cards.append(new_card)
    db.session.add(new_board)
    db.session.commit()
    return new_board

@pytest.fixture
def three_cards(app):
    new_board = Board(board_id=1, title="Life Goals", owner="Angie")
    new_card1 = Card(board_id=1, card_id=1, likes_count=0, message="Good things are coming!") 
    new_card2 = Card(board_id=1, card_id=2, likes_count=5, message="You are doing great!") 
    new_card3 = Card(board_id=1, card_id=3, likes_count=14, message="Don't forget to drink lots of water!")

    new_board.cards.append(new_card1)
    new_board.cards.append(new_card2)
    new_board.cards.append(new_card3)
    db.session.add(new_board)
    db.session.commit()
    return new_board