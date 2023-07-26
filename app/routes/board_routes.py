from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card
from app.models.board import Board
from .routes_helpers import validate_model

board_bp = Blueprint("boards", __name__, url_prefix="/boards")

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return make_response(jsonify(new_board.to_dict()), 201)


@board_bp.route("/<board_id>/cards", methods=["POST"])
def add_card_to_board(board_id):
    board = validate_model(Board, board_id)

    request_body = request.get_json()

    new_card = Card.from_dict(request_body)

    new_card.board_id = board.board_id

    db.session.add(new_card)
    db.session.commit()

    return make_response(jsonify(new_card.to_dict()), 201)
    

@board_bp.route("", methods=["GET"])
def get_all_boards():
    
    boards = Board.query.all()

    boards_response = [board.to_dict() for board in boards]

    def get_id(entry):
        return entry['board_id']
    
    boards_response.sort(key=get_id)
    
    return jsonify(boards_response), 200


@board_bp.route("/<board_id>",  methods=["GET"])
def get_one_board(board_id):
    board = validate_model(Board, board_id)

    response_body = {
        "board_id": board.board_id,
        "title": board.title,
        "owner": board.owner,
        }

    return jsonify(response_body), 200


@board_bp.route("/<board_id>/cards",  methods=["GET"])
def get_cards_of_one_board(board_id):
    board = validate_model(Board, board_id)

    cards_response = []
    for card in board.cards:
        cards_response.append(card.to_dict())

    def get_id(entry):
        return entry['card_id']
    
    cards_response.sort(key=get_id)

    return jsonify(cards_response), 200


@board_bp.route("/<board_id>",  methods=["DELETE"])
def delete_board(board_id):
    
    board = validate_model(Board, board_id)

    db.session.delete(board)
    db.session.commit()

    return make_response(jsonify({"message":f"Board {board_id} successfully deleted"}), 200)