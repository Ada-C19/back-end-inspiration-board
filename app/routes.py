from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card

# example_bp = Blueprint('example_bp', __name__)
cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

@cards_bp.route("", methods=["POST"])

def create_card():
    request_body = request.get_json()

    new_card = Card.from_dict(request_body)

    db.session.add(new_card)
    db.session.commit()

    return jsonify(new_card.to_dict()), 201