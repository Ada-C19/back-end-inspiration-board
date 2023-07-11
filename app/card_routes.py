from app import db
from flask import Blueprint, request, jsonify, make_response
from app.models.card import Card
from .route_helper import validate_model

bp = Blueprint('cards', __name__, url_prefix="/cards")

# update card endpoint
@bp.route("/<card_id>", methods=["PATCH"])
def add_like(card_id):
    card = validate_model(Card, card_id)

    card.likes_count += 1

    db.session.commit()

    response_body = dict(card=card.to_dict())

    return make_response(jsonify(response_body), 200)

# delete a card endpoint
@bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = validate_model(Card, card_id)
    db.session.delete(card)
    db.session.commit()

    response_body = dict(details=f'Card {card.id}: {card.message} successfully deleted')

    return make_response(jsonify(response_body), 200)    