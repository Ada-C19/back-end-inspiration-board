from flask import Blueprint, request, jsonify
from app import db
from app.models.board import Board
from app.models.card import Card 

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

# route to get one specific card
@cards_bp.route("/<card_id>", methods=["GET"])
def get_one_card(card_id):
    card = Card.query.get(card_id)
    card_response = Card.to_dict_cards(card)

    return jsonify(card_response), 200

# route to delete a card
@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = Card.query.get(card_id)

    db.session.delete(card)
    db.session.commit()

    return jsonify(f"Card with id {card.card_id} was deleted!"), 200

# route to update likes count 
@cards_bp.route("/<card_id>", methods=["PUT"])
def update_likes(card_id):
    card = Card.query.get(card_id)
    request_body = request.get_json()
    card.likes_count = request_body["likes_count"]

    db.session.commit()

    return jsonify(f"Card {card.card_id} now have {card.likes_count} likes."), 200

