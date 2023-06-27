from app import db
from app.models.board import Board
from app.models.card import Card
from flask import Blueprint, request, jsonify, make_response


boards_bp = Blueprint("boards", __name__, url_prefix="/boards")

@boards_bp.route("", methods=["POST"])
def create_board():
    pass

@boards_bp.route("", methods=["GET"])
def get_all_boards():
    pass

@boards_bp.route("/<board_id>", methods=["GET"])
def get_board(board_id):
    pass

@boards_bp.route("/<board_id>", methods=["DELETE"])
def delete_board(board_id):
    pass

@boards_bp.route("/<board_id>", methods=["PATCH"])
def update_board(board_id):
    pass

@boards_bp.route("/<board_id>/cards", methods=["POST"])
def create_card(board_id):
    pass

@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_all_cards(board_id):
    pass