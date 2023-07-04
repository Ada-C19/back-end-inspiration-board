from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card
from .routes_helpers import validate_model

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix="/boards")

@board_bp.route("", methods=["GET"])
def get_all_boards():
    boards = Board.query.all()
    boards_response = [board.to_dict() for board in boards]
    return make_response(jsonify(boards_response), 200)

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    try:
        new_board = Board.from_dict(request_body)
    except KeyError:
        abort(make_response(jsonify({"details": "Invalid data"}), 400))

    db.session.add(new_board)
    db.session.commit()

    return make_response(jsonify(new_board.to_dict()), 201)


# GET ALL TASKS FOR GOAL
@board_bp.route("/<id>/cards", methods=["GET"])
def get_board_cards(id):
    board = validate_model(Board, id)
    # just a list of cards, not all the board data
    card_response = [card.to_dict() for card in board.cards]
    return make_response(jsonify(card_response))

# create a route to add new card for selected board
@board_bp.route("/<id>/cards", methods=["POST"])
def create_card(id):
    request_body = request.get_json()
    request_body["board_id"] = id

    # need to add char count feedback
    try:
        new_card = Card.from_dict(request_body)
    except KeyError:
        abort(make_response(jsonify({"details": "Invalid data"}), 400))
    
    if len(new_card.message) > 40:
        abort(make_response(jsonify({
            "details": "Message should be 40 characters or less."
            }), 400))

    db.session.add(new_card)
    db.session.commit()

    return make_response(jsonify(new_card.to_dict()), 201)