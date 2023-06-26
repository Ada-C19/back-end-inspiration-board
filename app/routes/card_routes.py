from flask import Blueprint, request,jsonlify, make_response
from app import db
from app.models.card import card

cards_bp = Blueprint ("cards", __name__, url_prefix=("/cards"))

@cards_bp.route("", methods=["GET"])
def get_cards():
    cards = Card.query.all()