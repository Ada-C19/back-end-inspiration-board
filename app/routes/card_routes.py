from app import db
from app.models.board import Board
from app.models.card import Card
from flask import Blueprint, request, jsonify, make_response, abort
from app.routes.route_helpers import validate_model, create_item, \
    get_all_items, get_item, update_item, delete_item, update_likes


cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

@cards_bp.route("", methods=["GET"])
def get_all_cards():
    return get_all_items(Card)

@cards_bp.route("/<card_id>", methods=["GET"])
def get_card(card_id):
    return get_item(Card, card_id)

@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    return delete_item(Card, card_id)

@cards_bp.route("/<card_id>", methods=["PATCH"])
def update_card(card_id):
    return update_item(Card, card_id)

@cards_bp.route("/<card_id>/like", methods=["PATCH"])
def like_card(card_id):
    return update_likes(Card, card_id, 1)

@cards_bp.route("/<card_id>/unlike", methods=["PATCH"])
def unlike_card(card_id):
    return update_likes(Card, card_id, -1)