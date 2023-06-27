from flask import Blueprint, request, jsonify, make_response
from app import db
from .route_helpers import create_model, validate_model, update_model
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
    return make_response(jsonify(f"{new_card.message} successfully posted on {board.title}", 201))


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
    card_list = [card.to_dict() for card in board.cards]

    # do we want the board though or just the cards?
    # i could just return card.to_dict for each card in card_list 
    return make_response(board.to_dict(), 200)

# UPDATE
@board_bp.route("<board_id>", methods=["PUT"])
def update_board(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    update_model(board, request_body)
    db.session.commit()
    return make_response({"board": board.to_dict()}, 200)


# DELETE
@board_bp.route("<board_id>", methods=["DELETE"])
def delete_board(board_id):
    board = validate_model(Board, board_id)
    db.session.delete(board)
    db.session.commit()
    return make_response({"details": f"Board {board.id} \"{board.title}\" successfully deleted"}, 200)