from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix = "/boards")
card_bp = Blueprint("cards", __name__, url_prefix = "/cards")

#####   ---   BOARD ROUTES   -   #####
#  GET - Read ALL boards
@board_bp.route("", methods=["GET"])
def read_all_boards():
    boards_response = []               # initialize list to hold all boards returned
    boards = Board.query.all()         # call to get all Boards

    # calls make_board_dict helper function to populate Board class attributes for each board and appends to the list
    boards_response = [make_board_dict(board)for board in boards]

    return jsonify(boards_response)     # returns jsonify boards response

# GET - Read ONE board
@board_bp.route("/<board_id>", methods = ["GET"])
def read_board_by_id(board_id):
    board = validate_model(Board, board_id)     # helper function validate id and return board dict

    print("****** ", make_board_dict(board), " ******")
    return {"board": make_board_dict(board)}, 200    # returns board in dict form

# GET - Read ALL CARDS by Board id
@board_bp.route("/<board_id>/cards", methods = ["GET"])
def read_cards_by_board_id(board_id):
    cards_response = []
    board = validate_model(Board, board_id)

    cards_response = [make_card_dict(card) for card in board.cards]

    return jsonify ({
        "board id": board_id,
        "board title": board.title,
        "cards": cards_response
    })



#####   ---   CARD ROUTES   -   #####
#   GET - Read ALL cards
@card_bp.route("", methods = ["GET"])
def read_all_cards():
    cards_response = []                 # initialize list to hold all cards returned
    cards = Card.query.all()            # call to get all Cards

    # calls make_card_dict() to populate Card class attributes for each card and appends to list
    cards_response = [make_card_dict(card) for card in cards]
    
    return jsonify(cards_response)      # returns jsonify cards response
    
#   GET - Read ONE card
@card_bp.route("/<card_id>", methods = ["GET"])
def read_card_by_id(card_id):
    card = validate_model(card_id)
    
    return (f"{card_id}: ${make_card_dict(card)}")       # returns card # in dict form
    


#DELETE - Delete ONE card
@card_bp.route("/<board_id>/<card_id>", methods=["DELETE"])
def delete_card_by_id(card_id):
    card = validate_model(Card, card_id)
    db.session.delete(card)
    db.session.commit()
    return abort(make_response({"details":f"Card {card.card_id} successfully deleted"}))



#####   ---   HELPER FUNCTIONS   -   #####

# Validate Model ID
# Takes: Model Class Name, Class Infor from query
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


# Make Board into Dictionary
# note: eventually move to Board Class
#       Takes: board object from query
#       Returns: board dictionary
def make_board_dict(board):
    return dict(
        id=board.board_id,
        title=board.title,
        owner=board.owner)


# Make Card into Dictionary
# note: move to Card Class
#       Takes: card object from query
#       Returns: card dictionary
def make_card_dict(card):
    return dict(
        message = card.message,
        likes_count = card.likes_count
    )
