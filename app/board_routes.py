from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card
from app.helper import validate_model, validate_message

boards_bp = Blueprint('goals', __name__, url_prefix='/boards')

@boards_bp.route('', methods=['GET'])
def get_all_boards():
    boards = Board.query.all()

    boards_response = [board.to_dict() for board in boards]

    return jsonify(boards_response)

@boards_bp.route('/<board_id>', methods=['GET'])
def get_one_board(board_id):
    board = validate_model(Board, board_id)

    return jsonify(board.to_dict())

@boards_bp.route('', methods=['POST'])
def create_board():
    request_body = request.get_json()

    try:
        new_board = Board.from_dict(request_body)
        db.session.add(new_board)
        db.session.commit()

        return make_response({'board':new_board.to_dict()}, 201)
    except:
        abort(make_response({'details': 'Invalid data'}, 400))

@boards_bp.route('/<board_id>/cards', methods=['POST'])
def create_card(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    message = request_body.get("message")

    if validate_message(message):
        return validate_message()
    
    card = Card(message=message, likes_count=0, board_id=board.board_id)

    db.session.add(card)
    db.session.commit()

    return make_response({"id": board.board_id, "card_id": card.card_id}), 200


cards_bp = Blueprint('goals', __name__, url_prefix='/cards')


