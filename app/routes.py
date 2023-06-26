from flask import Blueprint, request, jsonify, abort, make_response
from app import db
from app.models.board import Board
from app.models.card import Card

# Helper Functions:
def validate_model(model_class, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({'message': f"{model_id} is not a valid type.  It must be an integer"}, 400))

    model = model_class.query.get(model_id)

    if not model:
        abort(make_response({'message': f'{model_id} does not exist'}, 404))

    return model

#example_bp = Blueprint('example_bp', __name__)
boards_bp = Blueprint("boards", __name__, url_prefix="/boards")
cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

# create a board
@boards_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    if request_body.get('owner') and request_body.get('title'):
        new_board = Board.from_dict(request_body)
    else:
        abort(make_response({"message": "Board input data incomplete"}, 400))
    
    db.session.add(new_board)
    db.session.commit()

    return jsonify(f"Board {new_board.id} successfully created."), 201

# get all boards
@boards_bp.route("", methods = ["GET"])
def get_boards():
    boards = Board.query.all()

    board_response = []
    for board in boards:
        board_response.append(board.to_dict())
    
    return jsonify(board_response), 200

# Create a new card for the selected board
@boards_bp.route("/<board_id>/cards", methods=["POST"])
def create_card_for_board(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    if len(request_body['message']) > 40:
        abort(make_response({"message": "Message was too long, keep it under 40 characters please"}, 400))

    new_card = Card(message=request_body['message'], board=board)

    db.session.add(new_card)
    db.session.commit()

    return jsonify('Card was successfully created'), 201

# get cards for board_id
@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_cards_for_board(board_id):
    board = validate_model(Board, board_id)
    cards = []
    for card in board.cards:
        cards.append(card.to_dict())

    return jsonify(cards), 200

# delete card 
@cards_bp.route('/<card_id>', methods=['DELETE'])
def delete_card(card_id):
    card = validate_model(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return jsonify('Card successfully deleted'), 201
