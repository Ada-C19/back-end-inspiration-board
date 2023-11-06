from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card
from app.helper import validate_model, validate_message

boards_bp = Blueprint('boards', __name__, url_prefix='/boards')

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

        errors = []

        if not new_board.title:
            errors.append({"field": "title", "message": "Title is required"})
            
        if not new_board.owner:
            errors.append({"field": "owner", "message": "Owner is required"})

        if errors:
            return make_response(jsonify(errors=errors), 400)

        db.session.add(new_board)
        db.session.commit()

        return make_response({'board': new_board.to_dict()}, 201)
    except:
        return make_response({'details': 'Invalid data'}, 400)

@boards_bp.route('/<board_id>', methods=['DELETE'])
def delete_board(board_id):
    board_to_delete = validate_model(Board, board_id)

    db.session.delete(board_to_delete)
    db.session.commit()

    message = f'Board {board_id} successfully deleted'
    return make_response({"details": message}, 200)

@boards_bp.route('/<board_id>/cards', methods=['POST'])
def create_card(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    message = request_body.get("message")

    validated_message = validate_message(message)
    if validated_message is not None:
        return validated_message
    
    card = Card(message=message, likes_count=0)

    db.session.add(card)
    db.session.commit()

    return make_response(card.to_dict()), 201

@boards_bp.route('/<board_id>/cards', methods=['GET'])
def get_all_cards(board_id):
    board = validate_model(Board, board_id)
    
    cards = Card.query.filter_by(board=board)
    
    cards_response = [card.to_dict() for card in cards]

    return jsonify(cards_response)
