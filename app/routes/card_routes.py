from flask import Blueprint, request, jsonify, make_response
from app import db
from ..models.card import Card

# example_bp = Blueprint('example_bp', __name__)
bp = Blueprint("cards", __name__, url_prefix="/cards")

# Read all cards:


@bp.route("", methods=["Get"])
def get_all_cards():
    cards_object = Card.query.all()
    card_list = [card.to_dict for card in cards_object]
    return make_response(jsonify(card_list), 200)

# Read one card:
