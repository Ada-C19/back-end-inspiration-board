from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
from .routes_helper import validate

boards_bp = Blueprint("boards", __name__, url_prefix="/boards")


@boards_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    if "title" not in request_body or "owner" not in request_body:
        return make_response({"details": "data not in request body"}, 400)

    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    response_body = {"boards": new_board.to_dict()}

    return jsonify(response_body), 201

@boards_bp.route("", methods=["GET"])
def get_all_boards():

    boards = Board.query.all()
    board_list = [board.to_dict() for board in boards]

    return jsonify(board_list), 200
