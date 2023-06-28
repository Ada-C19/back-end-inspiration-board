import pytest
from app import create_app
from app import db
from app.models.board import Board
from app.models.card import Card
from datetime import datetime
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

@pytest.fixture
def one_card(app):
    new_card = Card(
        message="Reminder to water plants", likes_count=2)
    db.session.add(new_card)
    db.session.commit()

@pytest.fixture
def three_cards(app):
    db.session.add_all([
        Card(message="Reminder to water plants", likes_count=2),
        Card(message="Reminder to do groceries", likes_count=1),
        Card(message="Reminder to take out trash", likes_count=3)
    ])
    db.session.commit()

@pytest.fixture
def one_board_belongs_to_one_card(app, one_board, one_card):
    card = Card.query.first()
    board = Board.query.first()
    board.cards.append(card)
    db.session.commit()


