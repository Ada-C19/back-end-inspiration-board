from flask import Blueprint, request, jsonify, make_response
from app import db
from route_helpers import create_model, validate_model
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


@board_bp.route("", methods=["GET"])
def get_specific_board(): 
    pass


@board_bp.route("", methods=["GET"])
def get_cards_from_board():
    pass

# UPDATE
@board_bp.route("", methods=["PUT"])
def update_board():
    pass


# DELETE
@board_bp.route("", methods=["DELETE"])
def delete_board():
    pass