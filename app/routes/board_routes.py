from app import db
from app.models.board import Board
from app.models.card import Card
from flask import Blueprint, request, jsonify, make_response, abort
from app.routes.route_helpers import validate_model, create_item, \
    get_all_items, get_item, update_item, delete_item


boards_bp = Blueprint("boards", __name__, url_prefix="/boards")

@boards_bp.route("", methods=["POST"])
def create_board():
    return create_item(Board)

@boards_bp.route("", methods=["GET"])
def get_all_boards():
    return get_all_items(Board)

@boards_bp.route("/<board_id>", methods=["GET"])
def get_board(board_id):
    return get_item(Board, board_id)

@boards_bp.route("/<board_id>", methods=["DELETE"])
def delete_board(board_id):
    return delete_item(Board, board_id)

@boards_bp.route("/<board_id>", methods=["PATCH"])
def update_board(board_id):
    return update_item(Board, board_id)

@boards_bp.route("/<board_id>/cards", methods=["POST"])
def create_card(board_id):
    request.json["board_id"] = board_id
    return create_item(Card)

@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_all_cards(board_id):
    result = get_item(Board, board_id)[0].get_json()['board']['cards']
    return jsonify(result), 200