from flask import Blueprint, request, jsonify, make_response
from app import db
from app.helper_functions import validate_model, validate_message
from app.models.board import Board
from app.models.card import Card

# example_bp = Blueprint('example_bp', __name__)
boards_bp = Blueprint("boards_bp", __name__, url_prefix="/boards")


@boards_bp.route('/<board_id>/cards', methods=['POST'])
def create_card(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json 
    message = request_body.get("message")

    if validate_message(message):
        return validate_message()
    
    card = Card(message=message)

    db.session.add(card)
    db.session.commit()

    return make_response({"id": board.board_id, "card_ids":request_body["card_ids"]}), 200