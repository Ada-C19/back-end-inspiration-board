from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix="/boards")
card_bp = Blueprint("cards", __name__, url_prefix="/cards")


#####   ---   HELPER FUNCTIONS   -   #####

# Validate Model ID
# Takes: Model Class Name, Class Info from query
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        abort(make_response(
            {"message": f"{model_id} is not a valid type. A {(type(model_id))} data type was provided. Must be a valid integer data type."}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} does not exist"}, 404))

    return model


#####   ---   BOARD ROUTES   -   #####
# POST - Create New Boards


@board_bp.route("", methods=["POST"])
def create_new_board():
    request_body = request.get_json()
    # validate board credentials
    if "title" not in request_body or "owner" not in request_body:
        return make_response({"details": "Invalid data. Must provide title and/or owner."}, 400)

    new_board = Board.from_dict(request_body)
    db.session.add(new_board)
    db.session.commit()

    return {"board": new_board.to_dict()}, 201


#  GET - Read ALL boards
@board_bp.route("", methods=["GET"])
def read_all_boards():
    boards = Board.query.all()         # call to get all Boards

    boards_response = [board.to_dict() for board in boards]

    return jsonify(boards_response)

# GET - Read ONE board


@board_bp.route("/<board_id>", methods=["GET"])
def read_board_by_id(board_id):
    # helper function validate id and return board dict
    board = validate_model(Board, board_id)

    return {"board": board.to_dict()}, 200

# GET - Read ALL CARDS by Board id


@board_bp.route("/<board_id>", methods=["PATCH"])
def read_update_board(board_id):
    # helper function validate id and return board dict
    board = validate_model(Board, board_id)
    request_body = request.get_json()

    if request_body["title"]:
        board.title = request_body["title"]
    if request_body["owner"]:
        board.owner = request_body["owner"]

    db.session.commit()

    return {"board": board.to_dict()}, 200


@board_bp.route("/<board_id>/cards", methods=["GET"])
def read_cards_by_board_id(board_id):
    board = validate_model(Board, board_id)

    cards_response = [card.to_dict() for card in board.cards]

    return {
        "board_id": board.board_id,
        "title": board.title,
        "owner": board.owner,
        "cards": cards_response
    }, 200


@board_bp.route("/<board_id>", methods=["DELETE"])
def delete_board_by_id(board_id):
    board = validate_model(Board, board_id)
    db.session.delete(board)
    db.session.commit()
    return make_response({"details": f"Board {board.board_id} successfully deleted"})

#####   ---   CARD ROUTES   -   #####
#   GET - Read ALL cards


@card_bp.route("", methods=["GET"])
def read_all_cards():
    cards_response = []                 # initialize list to hold all cards returned
    cards = Card.query.all()            # call to get all Cards

    # calls make_card_dict() to populate Card class attributes for each card and appends to list
    cards_response = [card.to_dict() for card in cards]

    return jsonify(cards_response)      # returns jsonify cards response

#   GET - Read ONE card


@card_bp.route("/<card_id>", methods=["GET"])
def read_card_by_id(card_id):
    card = validate_model(Card, card_id)

    # returns card # in dict form
    return {
        card.card_id: card.to_dict()
    }


@board_bp.route("/<board_id>/cards", methods=["POST"])
def create_card_by_id(board_id):

    board = validate_model(Board, board_id)

    request_body = request.get_json()

    new_card = Card(
        message=request_body["message"],
        board=board
    )

    db.session.add(new_card)
    db.session.commit()

    return {"card": new_card.to_dict()}, 201


@board_bp.route("/<board_id>/cards", methods=["PATCH"])
def update_card_title(board_id):
    board = validate_model(Board, board_id)
    # request_body = request.get_json()
    board.cards = []

    db.session.commit()
    return {
        "board": board.to_dict()}

# DELETE - Delete ONE card


@card_bp.route("/<card_id>", methods=["DELETE"])
def delete_card_by_id(card_id):
    card = validate_model(Card, card_id)
    db.session.delete(card)
    db.session.commit()
    return make_response({"details": f"Card {card.card_id} successfully deleted"}, 200)
