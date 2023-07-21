import pytest
from app import create_app
from app.models.card import Card
from app.models.board import Board
from app import db
from flask.signals import request_finished



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


#creates a card and saves it in the db

@pytest.fixture
def one_card(app):
    new_card = Card(
        board_id=None,
        likes_count=0,
        message="You got this"
        
    )
    db.session.add(new_card)
    db.session.commit()

#creates three careds and saves in db
@pytest.fixture
def three_cards(app):
    db.session.add_all([
        Card(
        message="You got this!"),
        Card(
        message="you fail if you dont take a chance!"),
        Card(
        message="and I oop")
    ])
    db.session.commit()

@pytest.fixture
def likes_count(app):
    new_card = Card(
        message="You got this!", likes_count=3)
    db.session.add(new_card)

### TESTING BOARD MODELS  ###
# Fixture creates a board and saves it to the db
# @pytest.fixture
# def one_board(app):
#     new_board = Board(title="Inspo board", owner="f-a-c-e")
#     db.session.add(new_board)
#     db.session.commit()
    
#Creates a board and card and it associates them with each other
#so that this board has a card and the card is in one goal
@pytest.fixture
def one_card_in_one_board(app, one_board, one_card):
    card = Card.query.first()
    board = Board.query.first()
    board.cards.append(card)
    db.session.commit()

@pytest.fixture
def one_board(app):
    new_board = Board(title="Encouraging quips", owner="f-a-c-e")
    db.session.add(new_board)
    db.session.commit()
