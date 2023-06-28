from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card
from sqlalchemy.types import DateTime
from sqlalchemy.sql.functions import now
from app.routes_helpers import validate_model
import requests, json
import os


# example_bp = Blueprint('example_bp', __name__)
boards_bp = Blueprint("boards", __name__, url_prefix="/boards")

@boards_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    is_valid_board_title = "title" in request_body
    is_valid_board_owner = "owner" in request_body
    if not is_valid_board_title:
        abort(make_response({"details": "Please include title"}, 400))
    if not is_valid_board_owner:
        abort(make_response({"details": "Please include owner"}, 400))

    new_board = Board.board_from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return make_response(jsonify(f"{new_board} successfully created!"), 201)

@boards_bp.route("", methods=["GET"])
def read_all_boards():
    boards = Board.query.all()
    boards_response = [board.board_to_dict() for board in boards]

    return jsonify(boards_response)

@boards_bp.route("/<board_id>", methods=["GET"])
def read_one_board(board_id):
    board = validate_model(Board, board_id)

    response_body = {
        "board": board.board_to_dict()
    }

    return jsonify(response_body)

@boards_bp.route("/<board_id>", methods=["DELETE"])
def delete_one_board(board_id):
    board = validate_model(Board, board_id)

    response_body = {
        "details": f"Board {board.id} \"{board.title}\" successfully deleted"
    }

    db.session.delete(board)
    db.session.commit()

    return jsonify(response_body)


@boards_bp.route("/<board_id>/cards", methods=["POST"])
def create_one_card_for_board(board_id):
    # board = validate_model(Board, board_id)
    board = Board.query.get(board_id)

    request_body = request.get_json()

    card = Card.query.get(request_body["id"])
    board.cards.append(card)

    db.session.add(board)
    db.session.commit()

    return make_response({
        "id": board.id,
        "card_id": request_body["id"]}, 200)


@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_cards_for_one_board(board_id):
    # board = validate_model(Board, board_id)
    board = Board.query.get(board_id)

    cards = board.cards

    cards_list = [card.card_to_dict() for card in cards]

    return make_response({
        "id": board.id,
        "title": board.title,
        "cards": cards_list}, 200)
