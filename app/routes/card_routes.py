from flask import Blueprint, request, jsonify, make_response
from app import db
from ..models.card import Card
from ..routes.helper import validate_model

# example_bp = Blueprint('example_bp', __name__)
bp = Blueprint("cards", __name__, url_prefix="/cards")


# Read all cards:
@bp.route("", methods=["Get"])
def get_all_cards():
    cards_object = Card.query.all()
    card_list = [card.to_dict() for card in cards_object]
    return make_response(jsonify(card_list), 200)


# Read one card:
@bp.route("/<card_id>", methods=["Get"])
def get_one_card(card_id):
    card_object = validate_model(Card, card_id)
    return make_response({"card": card_object.to_dict()}, 200)


# Create card:
@bp.route("", methods=["Post"])
def post_one_card():
    try:
        request_body_dict = request.get_json()
        card_object = Card.from_dict(request_body_dict)
        db.session.add(card_object)
        db.session.commit()
        return make_response({"card": card_object.to_dict()}, 201)
    except(KeyError):
        return make_response({"details": "Invalid data"}, 400)


# Delete a card:
@bp.route("/<card_id>", methods=["Delete"])
def delete_card(card_id):

    response_object = validate_model(Card, card_id)
    db.session.delete(response_object)
    db.session.commit()
    try:
        return make_response({"card": response_object.to_dict()}, 200)
    except(KeyError):
        return make_response({"details": "incomplete information"}, 400)


# Replace a card
@bp.route("/<card_id>", methods=["PUT"])
def replace_card(card_id):
    card_object = validate_model(Card, card_id)
    try:
        request_body = request.get_json()
        card_object.message = request_body["message"]
        card_object.likes_count = request_body["likes_count"]
        card_object.board_id = request_body["board_id"]
        db.session.commit()
        # =============================================================
        card_object = validate_model(Card, card_id)
        return make_response({"card": card_object.to_dict()}, 200)
    except(KeyError):
        return make_response(jsonify("incomplete information"), 400)

# Update a card


@bp.route("/<card_id>", methods=["PATCH"])
def update_card(card_id):
    card = validate_model(Card, card_id)
    request_body = request.get_json()
    flag = False
    if request_body.get("message"):
        flag = True
        card.message = request_body["message"]
    if request_body.get("likes_count"):
        flag = True
        card.likes_count = request_body["likes_count"]
    if request_body.get("board_id"):
        flag = True
        card.board_id = request_body["board_id"]
    db.session.commit()
    if flag:
        # =============================================================
        card_object = validate_model(Card, card_id)
        return make_response({"card": card_object.to_dict()}, 200)
    else:
        return make_response(jsonify(f"nothing was updated"))
