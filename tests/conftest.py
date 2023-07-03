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
def two_saved_boards(app):
    shakespeare_board = Board(title="Shakespeare Quotes",
                              owner="William Shakespeare")

    movie_board = Board(title="Movie Quotes",
                        owner="Meryl Streep")

    db.session.add_all([shakespeare_board, movie_board])
    db.session.commit()

    return shakespeare_board, movie_board


@pytest.fixture
def three_saved_cards(app):
    card_1 = Card(message="To be, or not to be, that is the question",
                  likes_count=5)
    card_2 = Card(message="Romeo, Romeo! Wherefore art thou Romeo?",
                  likes_count=3)
    card_3 = Card(message="There's no place like home.",
                  likes_count=2)

    db.session.add_all([card_1, card_2, card_3])
    db.session.commit()

    return card_1, card_2, card_3


@pytest.fixture
def three_saved_cards_and_two_boards(three_saved_cards, two_saved_boards):
    card_1, card_2, card_3 = three_saved_cards
    shakespeare_board, movies_board = two_saved_boards

    shakespeare_board.cards.extend([card_1, card_2])

    db.session.commit()

@pytest.fixture
def one_saved_card(app):
    card_1 = Card(message="To be, or not to be, that is the question",
                  likes_count=1)


    db.session.add_all([card_1])
    db.session.commit()

    return card_1


