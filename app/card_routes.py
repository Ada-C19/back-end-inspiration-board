from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.card import Card
from app.helper import validate_model, validate_message

cards_bp = Blueprint('cards', __name__, url_prefix='/cards')

@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card_to_delete = validate_model(Card, card_id)

    db.session.delete(card_to_delete)
    db.session.commit()

    message = f'Card {card_id} successfully deleted'
    return make_response({"details":message}, 200)