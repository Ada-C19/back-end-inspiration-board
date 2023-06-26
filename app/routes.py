from flask import Blueprint, request, jsonify, abort, make_response
from app import db
from app.models.board import Board
from app.models.card import Card

#example_bp = Blueprint('example_bp', __name__)
boards_bp = Blueprint("boards", __name__, url_prefix="/boards")

# create a board
@boards_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    if request_body.get('owner') and request_body.get('title'):
        new_board = Board.from_dict(request_body)
    else:
        abort(make_response({"message": "Board input data incomplete"}, 400))
    
    db.session.add(new_board)
    db.session.commit()

    return jsonify(f"Board {new_board.id} successfully created."), 201

# get all boards
@boards_bp.route("", methods = ["GET"])
def get_boards():
    boards = Board.query.all()

    board_response = []
    for board in boards:
        board_response.append(board.to_dict())
    
    return jsonify(board_response), 200