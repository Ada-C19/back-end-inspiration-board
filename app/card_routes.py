from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card 
from .route_helpers import validate_model

card_bp = Blueprint('card_bp', __name__, url_prefix="/cards")

# CREATE
@card_bp.route("", methods=["POST"])
def make_new_card():
    request_body = request.get_json()
    
    new_card = Card(message=request_body["message"])

    db.session.add(new_card)
    db.session.commit()
    
    return make_response(f"Card successfully created", 201)


# READ
@card_bp.route("", methods=["GET"])
def get_all_cards():

    cards = Card.query.all()

    cards_list=[card.make_card_dict()for card in cards]

    return jsonify(cards_list), 200


# UPATE
@card_bp.route("/<card_id>/like", methods=["PATCH"])
def like_card(card_id):
    card = validate_model(Card, card_id)
    card.likes_count += 1
    db.session.commit() 
    # return make_response(f"card {card.id} liked")
    return jsonify(card.make_card_dict())

# DELETE
@card_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = validate_model(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return make_response(f"Card successfully deleted")




