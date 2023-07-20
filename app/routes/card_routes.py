from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
from .routes_helper import validate, validate_card

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

#  unused route
# @cards_bp.route("", methods=["POST"])
# def create_card():
#     request_body = request.get_json()
#     if "message" not in request_body:
#         return make_response({"details": "data not in request body"}, 400)

#     new_card = Card.from_dict(request_body)

#     db.session.add(new_card)
#     db.session.commit()

#     response_body = {"cards": new_card.to_dict()}

#     return jsonify(response_body), 201


@cards_bp.route("", methods=["GET"])
def get_all_cards():

    cards = Card.query.all()
    cards_response = [card.to_dict() for card in cards]

    return jsonify(cards_response), 200


@cards_bp.route("/<model_id>", methods=["GET"])
def get_one_card(model_id):
    card = validate(Card, model_id)
    response_body = dict(card=card.to_dict())
    return jsonify(response_body), 200


@cards_bp.route("/<model_id>", methods=["DELETE"])
def delete_cards(model_id):
    card = validate(Card, model_id)

    db.session.delete(card)
    db.session.commit()

    return jsonify({"details": f'Card {model_id} "{card.message}" successfully deleted'}), 200


@cards_bp.route("/<model_id>/like", methods=["PUT"])
def likes(model_id):
    card = validate(Card, model_id)

    card.likes_count = card.likes_count + 1

    db.session.commit()

    response_body = dict(card=card.to_dict())

    return jsonify(response_body), 200


@cards_bp.route("/<model_id>/unlike", methods=["PUT"])
def unlikes(model_id):
    card = validate(Card, model_id)

    card.likes_count = card.likes_count - 1

    validate_card(card)

    db.session.commit()

    response_body = dict(card=card.to_dict())

    return jsonify(response_body), 200


@cards_bp.route("/<model_id>", methods=["PATCH"])
def update_cards(model_id):
    card = validate(Card, model_id)
    message = request.get_json()["message"]
    card.message = message

    validate_card(card)

    db.session.commit()

    response_body = dict(card=card.to_dict())

    return jsonify(response_body), 200
