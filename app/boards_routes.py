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

# validate board input
def validate_model_boards(cls, board_id):
    try:
        board_id = int(board_id)
    except:
        abort(make_response({"message": f"{cls.__name__} {board_id} invalid"}, 400))
    
    board = cls.query.get(board_id)