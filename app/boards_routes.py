from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card
from sqlalchemy.types import DateTime
from sqlalchemy.sql.functions import now
import requests, json
import os

# example_bp = Blueprint('example_bp', __name__)
boards_bp = Blueprint("boards", __name__, url_prefix="/boards")

# validate input
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{cls.__name__} {model_id} invalid"}, 400))
    
    model = cls.query.get(model_id)
    
    if not model:
        abort(make_response({"message": f"board {model_id} not found"}))
    

@boards_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()
    new_board = Board.board_from_dict(request_body)
    # new_board = Board(title=request_body["title"], owner=request_body["owner"])

    db.session.add(new_board)
    db.session.commit()

    return make_response(jsonify(f"{new_board} successfully created!"), 201)