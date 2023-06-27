from flask import Blueprint, request, jsonify, make_response
from app import db
from route_helpers import create_model, validate_model, update_model
from models.board import Board
from models.card import Card

board_bp = Blueprint('board_bp', __name__, url_prefix="/boards")


# CREATE
@board_bp.route("", methods=["POST"])
def post_board(): 
    request_body = request.get_json()
    new_board = create_model(Board, request_body)
    db.session.add(new_board)
    db.session.commit()
    return make_response({"board": new_board.to_dict()}, 201)


@board_bp.route("/<board_id>/cards", methods=["POST"])
def post_card_to_board(board_id):
    pass


# READ
@board_bp.route("", methods=["GET"])
def get_all_boards(): 
    pass


@board_bp.route("</board_id>", methods=["GET"])
def get_specific_board(board_id): 
    board = validate_model(Board, board_id)
    return make_response({"board": board.to_dict()}, 200)


@board_bp.route("", methods=["GET"])
def get_cards_from_board():
    pass

# UPDATE
@board_bp.route("/<board_id>", methods=["PUT"])
def update_board(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    update_model(board, request_body)
    db.session.commit()
    return make_response({"board": board.to_dict()}, 200)


# DELETE
@board_bp.route("/<board_id>", methods=["DELETE"])
def delete_board(board_id):
    board = validate_model(Board, board_id)
    db.session.delete(board)
    db.session.commit()
    return make_response({"details": f"Board {board.id} \"{board.title}\" successfully deleted"}, 200)