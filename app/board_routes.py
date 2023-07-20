from flask import Blueprint, request, jsonify, make_response
from app import db
from .route_helpers import create_model, validate_model
from app.models.board import Board
from app.models.card import Card

board_bp = Blueprint('board_bp', __name__, url_prefix="/boards")


# CREATE
@board_bp.route("", methods=["POST"])
def post_board(): 
    request_body = request.get_json()
    new_board = create_model(Board, request_body)
    db.session.add(new_board)
    db.session.commit()
    return make_response({"board": new_board.to_dict()}, 201)


@board_bp.route("<board_id>/cards", methods=["POST"])
def post_card_to_board(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()

    new_card = Card(
        message=request_body["message"],
        board = board
    )
    db.session.add(new_card)
    db.session.commit()
    return make_response(jsonify(f"{new_card.message} successfully posted on {board.title}"), 201)


# READ
@board_bp.route("", methods=["GET"])
def get_all_boards(): 
    boards = Board.query.all()
    boards_response = [board.to_dict() for board in boards]
    return jsonify(boards_response), 200


@board_bp.route("<board_id>", methods=["GET"])
def get_specific_board(board_id): 
    board = validate_model(Board, board_id)
    return make_response({"board": board.to_dict()}, 200)


@board_bp.route("<board_id>/cards", methods=["GET"])
def get_cards_from_board(board_id):
    board = validate_model(Board, board_id)
    card_list = [card.make_card_dict() for card in board.cards]
    return jsonify(card_list), 200


# DELETE
@board_bp.route("<board_id>", methods=["DELETE"])
def delete_board(board_id):
    board = validate_model(Board, board_id)
    db.session.delete(board)
    db.session.commit()
    return make_response({"details": f"Board {board.id} \"{board.title}\" successfully deleted"}, 200)