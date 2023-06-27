from app import db
from flask import Blueprint, request, jsonify, make_response
from app.models.board import Board
from app.models.card import Card

bp = Blueprint('boards', __name__, url_prefix="/boards")

# create a goal endpoint
@bp.route("", methods=["POST"])
def create_goal():
    request_body = request.get_json()

    new_goal = Board.from_dict(request_body)

    db.session.add(new_goal)
    db.session.commit()

    return jsonify({"goal": new_goal.to_dict()}), 201