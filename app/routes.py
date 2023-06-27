from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board

# example_bp = Blueprint('example_bp', __name__)

board_bp = Blueprint("boards", __name__, url_prefix="/boards")
from app.models.card import Card
from app.models.board import Board

# example_bp = Blueprint('example_bp', __name__)
cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"details":"Invalid data"}, 400))

    model = cls.query.get(model_id)
    
    if not model:
        abort(make_response({"details": f"{cls.__name__} {model_id} is not found"}, 404))
    
    return model


@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return {"Boards":new_board.to_dict()}, 201

@board_bp.route("", methods=["GET"])
def read_all_boards():
    boards = Board.query.all()
    boards_response = []

    for board in boards:
        boards_response.append(board.to_dict())

    return jsonify(boards_response), 200

@board_bp.route("/<board_id>", methods=["GET"])
def read_single_board(board_id):
    
    board = validate_model(Board, board_id)

    return board.to_dict(), 200


####### POST CARD TO SPECIFIC BOARD ##########
@cards_bp.route("/<board_id>", methods=["POST"])
def create_card(board_id):
    board_to_post = validate_model(Board, board_id)
    request_body = request.get_json()
    try:
        new_card = Card.from_dict(request_body)
        # Card.board = board_to_post
        new_card.board_id = board_to_post.board_id
    except:
        return jsonify({'details': 'Invalid card request body data'}), 400
    
    db.session.add(new_card)
    db.session.commit()
    
    return jsonify({"cards": f"{new_card.to_dict()} successfully created"}), 200

###### DELETE CARD ###############
@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card_to_delete = validate_model(Card, card_id)
    
    db.session.delete(card_to_delete)
    db.session.commit()
    
    return jsonify({"message": f"{card_to_delete} has been successfully deleted"}), 200

######## UPDATE CARD TO INCREASE LIKES ################
@cards_bp.route("/<card_id>/like", methods=["PUT"])
def update_card(card_id):
    card = validate_model(Card, card_id)
    
    request_body = request.get_json()
    
    card.likes_count = request_body["likes_count"]
    
    db.session.commit()
    
    return jsonify({"message": f"Increased like count on card {card.card_id}"}), 200
    
