from flask import Blueprint, request, jsonify, make_response
from app import db

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix="/boards")

# creates a new board
@board_bp.route("", methods=["POST"])
def create_board():
    pass

# displays all boards
@board_bp.route("", methods=["GET"])
def get_all_boards():
    pass

# displays all cards for one board
@board_bp.route("/<board_id>", methods=["GET"])
def get_one_board():
    pass

# deletes a board (and associated cards)
@board_bp.route("/<board_id>", methods=["DELETE"])
def delete_one_board():
    pass