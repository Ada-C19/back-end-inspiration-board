import pytest
from app import create_app
from app import db
from app.models.board import Board
from app.models.card import Card
from flask.signals import request_finished


@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

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
    new_board = Board(
        title="Movie Lovers",
        owner="Amethyst"
    )

    db.session.add(new_board)
    db.session.commit()


@pytest.fixture
def one_card(app):
    new_card = Card(
        message="Taylor Swift - Dear John!!! Stupid man!",
        likes_count=0,
    )

    db.session.add(new_card)
    db.session.commit()


@pytest.fixture
def one_board_with_one_card(app, one_board, one_card):
    card = Card.query.first()
    board = Board.query.first()
    board.cards.append(card)
    card.board_id = board.board_id
    db.session.commit()
