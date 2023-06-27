from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card

# example_bp = Blueprint('example_bp', __name__)

@board_bp('', methods=['POST'])
def create_board():
    request_body = request.get_json()

    try:
        new_board = Board.from_dict(request_body)
        db.session.add(new_board)
        db.session.commit()

        return make_response({'board':new_board.to_dict()}, 201)
    except:
        abort(make_response({'details': 'Invalid data'}, 400))