import pytest
from app import create_app
from app import db
from app.models.board import Board
from app.models.card import Card
#from flask.signals import request_finished


@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app(test_config=True)

    #@request_finished.connect_via(app)
    #def expire_session(sender, response, **extra):
     #   db.session.remove()

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
def two_saved_boards(client):
    board_1 = Board(owner = "Lindsay", title = "Shroomies")
    board_2 = Board(owner = "Stacy", title = "idk")

    db.session.add_all([board_1, board_2])
    db.session.commit()

@pytest.fixture
def one_saved_boards_with_two_cards(client):
    card_1 = Card(message = "card 1 message")
    card_2 = Card(message = "card 2 message")

    board_1 = Board(owner = "Lindsay", title = "Shroomies", cards = [card_1, card_2])

    db.session.add_all([board_1])
    db.session.commit()
