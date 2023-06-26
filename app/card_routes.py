from app import db
from flask import Blueprint, request, jsonify, make_response
from app.models.card import Card

bp = Blueprint('cards', __name__, url_prefix="/cards")

# create a card endpoint
# @bp.route("", methods=["POST"])

# get all cards endppint
# @bp.route("", methods=["GET"])

# get one card by ID endpoint
# @bp.route("/<card_id>", methods=["GET"])

# delete a card endpoint
# @bp.route("/<card_id>", methods=["DELETE"])

# update card endpoint
# @bp.route("/<card_id>", methods=["PUT"])
