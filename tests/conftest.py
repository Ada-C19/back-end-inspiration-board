import pytest
from app import create_app
from app.models.card import Card
from app.models.board import Board
from app import db
from flask.signals import request_finished

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def one_board(app):
    one_board = Board(
        title="New Board", owner="Genesis", id=1)
    db.session.add(one_board)
    db.session.commit()
    return one_board


@pytest.fixture
def one_card(app, one_board):
    one_card = Card(
        id=1,
        message="Yoga",
        likes_count=0,
        board_id=1)
    db.session.add(one_card)
    db.session.commit()
    return one_card








