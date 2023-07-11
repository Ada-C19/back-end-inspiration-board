from app import db
from flask import Blueprint, request, jsonify, make_response, abort
from app.models.board import Board
from app.models.card import Card
from .route_helper import validate_model, create_card, validate_message_length

bp = Blueprint('boards', __name__, url_prefix="/boards")

# CREATE
# create a board endpoint, returns 201 if successful
@bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return jsonify({"board": new_board.to_dict()}), 201

# READ
# Gets all Boards and returns 200
@bp.route("", methods=["GET"])
def read_all_boards():
    boards = Board.query.all()

    board_response = []
    for board in boards: 
        board_response.append(board.to_dict())
    return jsonify(board_response), 200

# Gets one board by board id and returns 200 if found
@bp.route("/<board_id>", methods=["GET"])
def read_one_board(board_id):
    board = validate_model(Board, board_id)
    response_body = board.to_dict()
    return jsonify(response_body), 200

# Gets cards by board_id
@bp.route("/<board_id>/cards", methods=["GET"])
def retrieve_cards(board_id): 
    board = validate_model(Board, board_id)

    cards_response = []
    for card in board.cards:
        cards_response.append(card.to_dict())
    return jsonify(cards_response), 200

# UPDATE
# assign cards to a board
@bp.route("/<board_id>/cards", methods=["POST"])
def add_cards_to_board(board_id):
    board = validate_model(Board, board_id)
    
    request_body = request.get_json()
    validate_message_length(request_body)
    card_id = create_card(request_body, board_id)
    
    card = validate_model(Card, card_id)
    board.cards.append(card)
    
    db.session.commit()

    return jsonify({"board_id": board.id, "card": card.to_dict()})


