from app import db
from app.models.board import Board
from app.models.card import Card
from flask import Blueprint, request, jsonify, make_response, abort


boards_bp = Blueprint("boards", __name__, url_prefix="/boards")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response(
            jsonify({"message": f"{cls.__name__} {model_id} invalid"}), 400))
        
    model = cls.query.get(model_id)
    if not model:
        abort(make_response(
            jsonify({"message": f"{cls.__name__} {model_id} not found"}), 400))
    
    return model 


@boards_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    try: 
        request_body["owner"] and request_body["title"] and request_body["description"]
    except: 
        abort(make_response(jsonify({"details": "Invalid data"}), 400))
    
    new_board = Board.from_dict(request_body)
    
    db.session.add(new_board)
    db.session.commit()

    response_body = {"board": new_board.to_dict()}

    return make_response(jsonify(response_body), 201)

@boards_bp.route("", methods=["GET"])
def get_all_boards():
    boards = Board.query.all()
    results = [board.to_dict() for board in boards]
    return jsonify(results)

@boards_bp.route("/<board_id>", methods=["GET"])
def get_board(board_id):
    board = validate_model(Board, board_id)
    response_body = {"board": board.to_dict()}
    return response_body

@boards_bp.route("/<board_id>", methods=["DELETE"])
def delete_board(board_id):
    board_to_delete = validate_model(Board, board_id)
    db.session.delete(board_to_delete)
    db.session.commit()
    response_body = {"details": f'Board {board_to_delete.id} "{board_to_delete.title}" succesfully deleted'}
    return response_body

@boards_bp.route("/<board_id>", methods=["PATCH"])
def update_board(board_id):
    board_to_update = validate_model(Board, board_id)
    board_updates = request.json()
    board_to_update.message = board_updates["message"]
    board_to_update.owner = board_updates["owner"]
    board_to_update.description = board_updates["description"]
    response_body = {board_to_update.to_dict()}
    db.session.commit()
    return response_body


@boards_bp.route("/<board_id>/cards", methods=["POST"])
def create_card(board_id):
    request_body = request.get_json()
    new_card = Card.from_dict(request_body)
    
    db.session.add(new_card)
    db.session.commit()

    response_body = {"board": new_card.to_dict()}

    return make_response(jsonify(response_body), 201)

@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_all_cards(board_id):
    board = validate_model(Board, board_id)
    response_body = board.to_dict(cards = True)
    return make_response(jsonify(response_body))