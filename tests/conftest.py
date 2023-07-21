import pytest
from app import create_app
from app.models.board import Board
from app.models.card import Card
from app import db
from datetime import datetime
import freezegun
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

# This fixture gets called in every test that
# references "one_board"
# This fixture creates a board and saves it in the database
@pytest.fixture
def one_board(app):
    with freezegun.freeze_time("2023-06-01 12:00:00"):
        board = Board(
            title="Test Board", 
            owner="Test Owner", 
            description="Test Description", 
            date_created=datetime.now(),
            theme="Test Theme"
        )
        db.session.add(board)
        db.session.commit()

# This fixture gets called in every test that
# references "three_boards"
# This fixture creates three boards and saves
# them in the database
@pytest.fixture
def three_boards(app):
    with freezegun.freeze_time("2023-06-01 12:00:00"):
        board1 = Board(
            title="Test Board 1", 
            owner="Test Owner 1",
            description="Test Description 1",
            date_created=datetime.now(),
            theme="Test Theme 1"
        )
        board2 = Board(
            title="Test Board 2",
            owner="Test Owner 2",
            description="Test Description 2",
            date_created=datetime.now(),
            theme="Test Theme 2"
        )
        board3 = Board(
            title="Test Board 3",
            owner="Test Owner 3",
            description="Test Description 3",
            date_created=datetime.now(),
            theme="Test Theme 3"
        )
        db.session.add_all([board1, board2, board3])
        db.session.commit()

# This fixture gets called in every test that
# references "one_card"
# This fixture creates a card and saves it in the database
@pytest.fixture
def one_card(app):
    with freezegun.freeze_time("2023-06-01 12:00:00"):
        card = Card(
            message="Test Message",
            date_created=datetime.now(),
            likes_count=0,
            board_id=1
        )
        db.session.add(card)
        db.session.commit()

# This fixture gets called in every test that
# references "three_cards"
# This fixture creates three cards and saves
# them in the database
@pytest.fixture
def three_cards(app):
    with freezegun.freeze_time("2023-06-01 12:00:00"):
        card1 = Card(
            message="Test Message 1",
            date_created=datetime.now(),
            likes_count=0,
            board_id=1
        )
        card2 = Card(
            message="Test Message 2",
            date_created=datetime.now(),
            likes_count=0,
            board_id=1
        )
        card3 = Card(
            message="Test Message 3",
            date_created=datetime.now(),
            likes_count=0,
            board_id=1
        )
        db.session.add_all([card1, card2, card3])
        db.session.commit()

# This fixture gets called in every test that
# references "one_board_with_one_card"
# This fixture creates a board and a card
# It associates the board and card, so that the
# board has this card, and the card belongs to one board
@pytest.fixture
def one_board_with_one_card(app, one_board, one_card):
    card = Card.query.first()
    board = Board.query.first()
    board.cards.append(card)
    db.session.commit()

# This fixture gets called in every test that
# references "one_board_with_three_cards"
# This fixture creates a board and three cards
# It associates the board and cards, so that the
# board has these cards, and the cards belong to one board
@pytest.fixture
def one_board_with_three_cards(app, one_board, three_cards):
    cards = Card.query.all()
    board = Board.query.first()
    board.cards.extend(cards)
    db.session.commit()
