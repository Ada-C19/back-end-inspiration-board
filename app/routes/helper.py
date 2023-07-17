from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"details": "Invalid data"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"details": "data not found"}, 404))

    return model


def validate_ids(board_id, card_id):
    board = validate_model(Board, board_id)
    try:
        card_id = int(card_id)
    except:
        abort(make_response({"details": "Invalid card_id"}, 400))
    return board
