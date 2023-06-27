import pytest
from app import create_app
from app import db
from app.models.card import Card
from app.models.board import Board
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
def one_card(app):
        card = Card(
            message="Here we are... Struggling, Yay!",
            likes_count=0,
            board_id=1
        )
        db.session.add(card)
        db.session.commit()


@pytest.fixture
def three_cards(app):
    db.session.add_all([
        Card(
            message="First message",
            likes_count=0,
            board_id=1
        ),
        Card(
            message="Second message",
            likes_count=0,
            board_id=1
        ),
        Card(
            message="Third message",
            likes_count=0,
            board_id=1
        )
        ])

    db.session.commit()


@pytest.fixture
def one_board(app):
    new_board = Board(
        title="test title", 
        owner="test owner")
    db.session.add(new_board)
    db.session.commit()


@pytest.fixture
def three_boards(app):
        db.session.add_all([  
        Board(
            title="First title", 
            owner="First Owner"
        ),
        Board(
            title="Second title",
            owner="Second Owner"
        ),
        Board(
            title="Third title",
            owner="Third Owner"
        )
        ])

        db.session.commit()


@pytest.fixture
def one_card_belongs_to_one_board(app, one_board, one_card):
    card = Card.query.first()
    board = Board.query.first()
    board.cards.append(card)
    db.session.commit()


@pytest.fixture
def one_board_with_three_cards(app, one_board, three_cards):
    cards = Card.query.all()
    board = Board.query.first()
    board.cards.extend(cards)
    db.session.commit()