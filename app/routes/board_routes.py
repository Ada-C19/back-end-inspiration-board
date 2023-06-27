from flask import Blueprint, request, jsonify, make_response
from app import db

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix="/boards")

# creates a new board
@board_bp.route("", methods=["POST"])
def create_board():
    pass