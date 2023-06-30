from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card
from ..routes.helper import validate_model

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("board", __name__, url_prefix="/boards")


# CREATE
@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    try:
        new_board = Board.from_board_dict(request_body)
        db.session.add(new_board)
        db.session.commit()
        return make_response(jsonify({"board": new_board.to_dict()}), 201)
    except KeyError as error:
        abort(make_response(
            {"details": "Cannot create board. Invalid data."}, 400))


# READ
@board_bp.route("", methods=["GET"])
def read_all_boards():
    boards = Board.query.all()
    boards_response = [board.to_dict() for board in boards]

    return jsonify(boards_response)


@board_bp.route("/<board_id>", methods=["GET"])
def read_one_board(board_id):
    board = validate_model(Board, board_id)
    return jsonify({"board": board.to_dict()})


# DELETE
@board_bp.route("/<board_id>", methods=["DELETE"])
def delete_board(board_id):
    board = validate_model(Board, board_id)
    db.session.delete(board)
    db.session.commit()
    return jsonify({"board": board.to_dict()})


# ONE-TO-MANY
@board_bp.route("/<board_id>/cards", methods=["POST"])
def post_card_to_board(board_id):
    try:
        board = validate_model(Board, board_id)
        request_body = request.get_json()
        new_card = Card.from_dict(request_body)
        if new_card.board_id == board.board_id:
            db.session.add(new_card)
            db.session.commit()
            return make_response({"id": board.board_id, "title": board.title, "card": new_card.to_dict()}, 201)
        return "Error: Invalid board_id"
    except(KeyError):
        return make_response({"details": "Invalid data"}, 400)


@board_bp.route("/<board_id>/cards", methods=["GET"])
def read_cards_on_board(board_id):
    try:
        board = validate_model(Board, board_id)
        cards_response = []
        for card in board.cards:
            cards_response.append(card.to_dict())
        return jsonify({"id": board.board_id, "cards": cards_response, "title": board.title}), 200

    except KeyError as error:
        abort(make_response({"details": "Data not found"}, 404))
