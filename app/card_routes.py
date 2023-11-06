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
    return make_response({"details": message}, 200)

@cards_bp.route("/<card_id>/increase", methods=["PATCH"])
def increase_likes(card_id):
    card = validate_model(Card, card_id)

    card.likes_count += 1

    db.session.commit()
    return jsonify(card.to_dict()), 200

@cards_bp.route("/<card_id>/decrease", methods=["PATCH"])
def decrease_likes(card_id):
    card = validate_model(Card, card_id)

    if card.likes_count > 0:
        card.likes_count -= 1

    db.session.commit()
    return jsonify(card.to_dict())

@cards_bp.route("/<card_id>", methods=["PATCH"])
def update_card_message(card_id):
    card = validate_model(Card, card_id)

    new_message = request.json.get("message")

    validated_new_message = validate_message(new_message)
    if validated_new_message is not None:
        return validated_new_message
    
    card.message = new_message

    db.session.commit()
    return jsonify(card.to_dict()), 200


    