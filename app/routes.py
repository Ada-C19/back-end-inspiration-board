from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card
from app.models.board import Board

# example_bp = Blueprint('example_bp', __name__)
card_bp = Blueprint("cards", __name__, url_prefix="/cards")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{model_id} is not a vlid type ({type(model_id)})"}))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} does not exist"}, 404))

    return model    


@card_bp.route("", methods=["POST"])
def create_card():
    request_body = request.get_json()

    new_card = Card.from_dict(request_body)

    db.session.add(new_card)
    db.session.commit()

    return jsonify(new_card.to_dict()), 201


@card_bp.route("", methods=["GET"])
def read_all_cards():
    board_query = request.args.get("board")

    if board_query:
        cards = Card.query.filter_by(board=board_query)

    cards_response = []

    for card in cards:
        cards_response.append(card.to_dict())

    return jsonify(cards_response)


@card_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = validate_model(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return make_response(f"Card #{card_id} successfully deleted")

from app.models.board import Board

# example_bp = Blueprint('example_bp', __name__)
board_bp =Blueprint("boards", __name__, url_prefix="/boards" )


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{model_id} invalid type ({type(model_id)})"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{model_id} invalid"}, 400))

    return model


# CREATE new board
@board_bp.route("", methods=["POST"])
def create_new_board():
    request_body = request.get_json()
    
    # pass in request_body
    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return jsonify(f"Board {new_board.title} successfully created"), 201


# READ all boards
@board_bp.route("", methods=["GET"])
def read_all_boards():
    boards_response = []

    board_title_query = request.args.get("title")
    board_owner_query = request.args.get("owner")

    if board_title_query:
        boards = Board.query.filter_by(title=board_title_query)
    elif board_owner_query: 
        boards = Board.query.filter_by(owner=board_owner_query)
    else: 
        boards = Board.query.all()

    for board in boards:
        boards_response.append(board.to_dict())
    return jsonify(boards_response)


# READ a specific board
@board_bp.route("/<board_id>", methods=["GET"])
def read_one_board(board_id):
    board = validate_model(Board, board_id)

    return board.to_dict(), 200