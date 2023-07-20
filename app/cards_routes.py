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

    new_card_id = new_card.id

    return make_response(jsonify({"id": new_card_id, "message": "Card successfully created"}), 201)

@cards_bp.route("", methods=["GET"])
def read_all_cards():
    cards = Card.query.all()

    cards_response = [card.card_to_dict() for card in cards]

    return make_response(jsonify(cards_response), 200)

@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_one_board(card_id):
    card = validate_model(Card, card_id)

    response_body = {
        "details": f"Card {card.id} \"{card.message}\" successfully deleted"
    }

    db.session.delete(card)
    db.session.commit()

    return jsonify(response_body)

@cards_bp.route("", methods=["DELETE"])
def delete_all_cards():
    cards = Card.query.all()
    for card in cards:
        db.session.delete(card)
    db.session.commit()

    return make_response(jsonify("All cards successfully deleted!"), 200)

@cards_bp.route("/<card_id>", methods=["PATCH"])
def increase_like_count(card_id):
    card = validate_model(Card, card_id)
    
    card.likes_count += 1

    db.session.commit()
    return make_response(card.card_to_dict(), 200)