from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.routes.helper_functions import validate_model


# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix="/boards")

# creates a new board
@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    try:
        new_board = Board.from_dict(request_body)
        db.session.add(new_board)
        db.session.commit()
        return make_response({"board": new_board.to_dict()}, 201)
    except KeyError:
        abort(make_response({"Invalid data"}, 400))
    

# displays all boards
@board_bp.route("", methods=["GET"])
def get_all_boards():
    boards = Board.query.all()
    board_response = [board.to_dict() for board in boards]
    return jsonify(board_response)

# displays all cards for one board
# test after making card routes
@board_bp.route("/<board_id>", methods=["GET"])
def get_one_board_and_cards(board_id):
    board = validate_model(Board, board_id)
    board_dict = board.get_cards()
    return make_response(board_dict, 200)

# deletes a board (and associated cards)
# have to maunally delete all cards
@board_bp.route("/<board_id>", methods=["DELETE"])
def delete_one_board():
    pass