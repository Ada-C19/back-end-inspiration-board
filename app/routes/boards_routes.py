from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card 


boards_bp = Blueprint("boards", __name__, url_prefix="/boards")

#route to get all boards
@boards_bp.route("",methods=["GET"])
def read_all_boards():
    boards = Board.query.all()
    board_response = []
    for board in boards:
        board_response.append(board.todict())
    
    return jsonify(board_response), 200


@boards_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    
    new_board = Board.from_dict_boards(request_body)
    
    db.session.add(new_board)
    db.session.commit()

    
    return make_response(jsonify({"board": new_board.to_dict_boards()}),201)

@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_cards_for_specific_board(board_id):

    boards_cards = {
        "id": board.board_id,
        "title": board.title,
        "cards": []
    }

    for card in board.cards:
        boards_cards["cards"].append(card.to_dict_cards
        ())

    return jsonify(boards_cards), 200