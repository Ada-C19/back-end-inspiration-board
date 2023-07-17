from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card
from ..routes.helper import validate_model, validate_ids

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
# Get all cards associated to a board
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

# read one card


@board_bp.route("/<board_id>/cards/<card_id>", methods=["GET"])
def get_one_card(card_id, board_id):
    card_object = validate_model(Card, card_id)
    return make_response({"card": card_object.to_dict()}, 200)


# post a card to a board
@board_bp.route("/<board_id>/cards", methods=["POST"])
def post_card_to_board(board_id):
    try:
        board = validate_model(Board, board_id)
        request_body = request.get_json()
        new_card = Card.from_dict(request_body)
        db.session.add(new_card)
        db.session.commit()
        return make_response({"id": board.board_id, "title": board.title, "card": new_card.to_dict()}, 201)
    except(KeyError):
        return make_response({"details": "Invalid data"}, 400)


# Delete a card:
@board_bp.route("/<board_id>/cards/<card_id>", methods=["Delete"])
def delete_card(card_id, board_id):
    card = validate_model(Card, card_id)
    db.session.delete(card)
    db.session.commit()
    return make_response({"card": card.to_dict()}, 200)

# Update a card- mark like
# like count update PATCH


@board_bp.route("/<board_id>/cards/<card_id>/mark_like", methods=["PATCH"])
def mark_like(card_id, board_id):
    card = validate_model(Card, card_id)
    card.likes_count = card.likes_count + 1
    db.session.commit()
    return make_response({"card": card.to_dict()}, 200)


# Update a card- mark unlike
@board_bp.route("/<board_id>/cards/<card_id>/mark_unlike", methods=["PATCH"])
def mark_unlike(card_id, board_id):
    card = validate_model(Card, card_id)
    card.likes_count = card.likes_count - 1
    db.session.commit()
    return make_response({"card": card.to_dict()}, 200)


# === if we want to add "edit" button
# Replace a card
# @board_bp.route("/<board_id>/cards/<card_id>", methods=["PUT"])
# def replace_card(card_id, board_id):
#     card = validate_model(Card, card_id)

#     request_body = request.get_json()
#     for card in board.cards:
#         if card.card_id == card_id:
#             try:
#                 card.message = request_body["message"]
#                 card.likes_count = request_body["likes_count"]
#                 card.board_id = request_body["board_id"]
#                 db.session.commit()
#                 return make_response({"card": card.to_dict()}, 200)
#             except:
#                 return make_response(jsonify("incomplete information"), 400)

#     abort(make_response({"details": "Card not found"}, 404))
