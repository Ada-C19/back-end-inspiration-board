from flask import jsonify, abort, make_response
from app.models.board import Board
from app.models.card import Card


def validate(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        response_str = f"{cls.__name__} {model_id} invalid"
        abort(make_response(jsonify({"message":response_str}), 400))

    matching_obj = cls.query.get(model_id)

    if not matching_obj:
        response_str = f"{cls.__name__.lower()} {model_id} not found"
        abort(make_response(jsonify({"message":response_str}), 404))

    return matching_obj


def validate_card(card: Card):
    msg_len = len(card.message)
    if msg_len < 1 or msg_len > 100:
        abort(make_response(jsonify({"message": "details: invalid data"}), 400))

def validate_board(board: Board):
    title_len = len(board.title)
    owner_len = len(board.owner)
    if title_len < 1 or owner_len < 1:
        abort(make_response(jsonify({"message": "details: invalid data"}), 400))