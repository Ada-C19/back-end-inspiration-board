from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
from app.helper import validate_model

boards_bp = Blueprint('goals', __name__, url_prefix='/boards')

@boards_bp.route('', methods=['GET'])
def get_all_boards():
    boards = Board.query.all()

    boards_response = [board.to_dict() for board in boards]

    return jsonify(boards_response)

@boards_bp.route('/<board_id>', methods=['GET'])
def get_one_board(board_id):
    board = validate_model(Board, board_id)

    return jsonify(board.to_dict())