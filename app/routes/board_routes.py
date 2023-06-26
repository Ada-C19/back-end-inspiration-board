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

@boards_bp.route("/<board_id>", methods=["GET"])
def get_one_board(board_id):
    board = validate(Board,board_id)
    response_body = dict(board = board.to_dict())

    return jsonify(response_body), 200


# create end point that retrieves and posts cards by goal_id
# ask if we need to create delete, put and patch endpoints


@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_board_cards(board_id):
    board = validate(Board,board_id)

    cards = Card.query.filter(Card.board_id == board.board_id)
    cards_response = [card.to_dict() for card in cards]

    return jsonify(cards_response), 200


# @boards_bp.route("/<board_id>", methods=["DELETE"])
# def delete_boards(board_id):
#     board = validate(Board, board_id)

#     db.session.delete(board)
#     db.session.commit()

#     return jsonify({"details": f'Board {board_id} "{board.title}"successfully deleted'}), 200