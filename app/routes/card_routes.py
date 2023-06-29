from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.card import Card
from app.models.board import Board
from app.routes.helper_functions import validate_model

# example_bp = Blueprint('example_bp', __name__)
card_bp = Blueprint("cards", __name__, url_prefix="/cards")

@card_bp.route("", methods=["POST"])
def create_card_for_board():
    request_body = request.get_json()
    board = validate_model(Board, request_body.get("board_id"))
    try:
        new_card = Card.from_dict(request_body)
        new_card.board_id = board.board_id
        db.session.add(new_card)
        db.session.commit()
        return make_response({"card": new_card.to_dict()}, 201)
    except KeyError:
        abort(make_response({"details":"Invalid data"}, 400))

@card_bp.route("<card_id>", methods=["PATCH"])
def update_one_card_likes():
    pass

@card_bp.route("<card_id>", methods=["DELETE"])
def delete_one_card():
    pass