from flask import Blueprint, jsonify, request
from app.models.board import Board
from app.models.card import Card
from app.routes.helpers import validate_model
from app import db

board_bp = Blueprint('board', __name__, url_prefix='/boards')

@board_bp.route('', methods=['GET'])
def get_boards():
    boards = Board.query.all()
    board_list = [board.to_json() for board in boards]
    return jsonify(board_list), 200

@board_bp.route('', methods=['POST'])
def create_board():
    data = request.get_json()
    board = Board.from_dict(data)

    db.session.add(board)
    db.session.commit()
    return jsonify({'message': 'Board created successfully'}), 201

@board_bp.route('/<board_id>', methods=['GET'])
def get_board(board_id):
    board = validate_model(Board, board_id)
    return jsonify(board.to_json())

@board_bp.route('/<board_id>', methods=['DELETE'])
def delete_board(board_id):
    board = validate_model(Board, board_id)

    db.session.delete(board)
    db.session.commit()

    return jsonify({'message': 'Board deleted successfully'}), 201

@board_bp.route('/<board_id>/cards', methods=['GET'])
def get_board_cards(board_id):
    board = validate_model(Board, board_id)
    cards = board.cards
    card_list = [card.to_json() for card in cards]
    
    return jsonify(card_list)

@board_bp.route('/<board_id>/cards', methods=['POST'])
def create_board_card(board_id):
    board = validate_model(Board, board_id)
    data = request.json
    message = data.get("message")
    card = Card(message=message, likes_count=0, board_id=board_id)
    
    db.session.add(card)
    db.session.commit()

    return jsonify({"message": "Card created successfully"}), 201
