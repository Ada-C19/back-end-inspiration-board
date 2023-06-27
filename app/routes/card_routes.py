from app import db
from app.models.board import Board
from app.models.card import Card
from flask import Blueprint, request, jsonify, make_response


cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

@cards_bp.route("", methods=["GET"])
def get_all_cards():
    pass

@cards_bp.route("/<card_id>", methods=["GET"])
def get_card(card_id):
    pass

@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    pass

@cards_bp.route("/<card_id>", methods=["PATCH"])
def update_card(card_id):
    pass

# @cards_bp.route("/<card_id>/like", methods=["PATCH"])
# def like_card(card_id):
#     pass