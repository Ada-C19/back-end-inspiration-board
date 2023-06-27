from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card
from app.routes_helpers import validate_model


cards_bp = Blueprint("cards", __name__, url_prefix="/cards")


@cards_bp.route("", methods=["POST"])
def create_card():
    request_body = request.get_json()

    new_card = Card.card_from_dict(request_body)

    db.session.add(new_card)
    db.session.commit()

    return make_response(f"Card successfully created", 201)


@cards_bp.route("", methods=["GET"])
def read_all_cards():
    cards = Card.query.all()

    cards_response = [card.card_to_dict() for card in cards]

    return make_response(jsonify(cards_response), 200)