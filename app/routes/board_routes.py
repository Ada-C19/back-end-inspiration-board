from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board

board_bp = Blueprint("boards", __name__, url_prefix="/boards")

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return make_response(jsonify({"board": new_board.to_dict()}), 201)


@board_bp.route("", methods=["GET"])
def read_all_boards():
    
    boards = Board.query.all()

    boards_response = [board.to_dict() for board in boards]
    
    return jsonify(boards_response), 200
