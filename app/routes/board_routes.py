from flask import Blueprint, jsonify, abort, make_response, request
from flask import Response
from app import db
from app.models.board import Board
from app.models.card import Card


board_bp = Blueprint("board_bp", __name__, url_prefix="/board")


def validate_model(cls, id):
    try:
        id = int(id)
    except:
        abort(make_response(
            {"message": f"{cls.__name__} {id} is invalid"}, 400))
    model = cls.query.get(id)
    if not model:
        abort(make_response(
            {"message": f"{cls.__name__} {id} not found"}, 404))

    return model


@board_bp.route('', methods=['POST'])
def create_board():
    request_body = request.get_json()
    try:
        new_board = Board.from_dict(request_body)
        db.session.add(new_board)
        db.session.commit()
        return make_response(request_body, 201)
    except KeyError:
        details = {"details": "Invalid data"}

        abort(make_response(details, 400))


@board_bp.route('', methods=['GET'])
def get_all_boards():
    boards = Board.query.all()
    board_response = []
    for board in boards:
        board_response.append(board.to_dict())
    return jsonify(board_response)


@board_bp.route('/<board_id>', methods=['PUT'])
def update_board(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    board.title = request_body['title']
    board.owner = request_body['owner']

    db.session.commit()
    response_dict = board.to_dict()
    return response_dict


@board_bp.route('/<board_id>', methods=['DELETE'])
def delete_board(board_id):
    board = validate_model(Board,board_id)
    db.session.delete(board)
    db.session.commit()
    return  {
        "details": f'Board {board_id} "{board.title}" successfully deleted'
    }


@board_bp.route("<board_id>/cards", methods=["POST"])
def create_card(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    try:
        new_card = Card.from_dict(request_body)
        new_card.board = board
        if len(new_card.message) > 40:
            return make_response({"Error": "Expected length exceeded"})

        db.session.add(new_card)
        db.session.commit()

       
        return make_response(new_card.to_dict(), 201)
    except KeyError as e:
        abort(make_response({"message": f"missing required value: {e}"}, 400))


@board_bp.route("<board_id>/cards", methods=["GET"])
def read_cards(board_id):
    board = validate_model(Board, board_id)

    cards_response = []
    for card in board.cards:
        cards_response.append(card.to_dict())
    return(jsonify(cards_response))


