from flask import Blueprint, request, jsonify, make_response, abort
import requests
from app import db
from app.models.board import Board
from app.models.card import Card
import os

boards_bp = Blueprint("boards", __name__, url_prefix="/boards")

# route to get all boards
@boards_bp.route("", methods=["GET"])
def get_all_boards():
    boards = Board.query.all()
    board_response = []
    for board in boards:
        board_response.append(board.to_dict_boards())

    return jsonify(board_response), 200

# route to get one board
@boards_bp.route("/<board_id>", methods=["GET"])
def get_one_board(board_id):
    board = Board.query.get(board_id)
    board_response = Board.to_dict_boards(board)

    return jsonify(board_response), 200

# route to post a new board
@boards_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    new_board = Board.from_dict_boards(request_body)

    db.session.add(new_board)
    db.session.commit()

    return jsonify(f"New board with id {new_board.board_id} was created!"), 201

# route to get cards of a board
@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_cards_for_specific_board(board_id):
    board = Board.query.get(board_id)
    cards_list = []

    for card in board.cards:
        cards_list.append(card.to_dict_cards())

    return jsonify(cards_list), 200

# route to post new card to a specific board
@boards_bp.route("/<board_id>/cards", methods=["POST"])
def post_cards_for_specific_board(board_id):

    request_body = request.get_json()
    board = Board.query.get(board_id)

    new_card = Card(message=request_body["message"], board=board)

    if len(request_body["message"]) > 40: 
        abort(make_response({"Error":"Message length must be less than 40 characters."}, 400))
        
    db.session.add(new_card)
    db.session.commit()

    slack_notification(new_card)

    return jsonify(f"A card with id {new_card.card_id} was added to Board {new_card.board.title}!"), 201

def slack_notification(new_card):
    token = os.environ.get("slack_token")
    slack_url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization":token}
    body = {
        "channel": "inspiration-board",
        "text": f"Someone just added a card with the message {new_card.message}", 
    }

    requests.post(slack_url, headers=headers, json=body)
    return

# route to delete one board
@boards_bp.route("/<board_id>", methods=["DELETE"])
def delete_board(board_id):
    board = Board.query.get(board_id)

    db.session.delete(board)
    db.session.commit()

    return jsonify(f"Board with id {board.board_id} was deleted!"), 200

