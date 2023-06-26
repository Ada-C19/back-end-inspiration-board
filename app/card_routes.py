from flask import Blueprint, request, jsonify, make_response
from app import db

cards_bp = Blueprint('cards', __name__, url_prefix="/cards")

# create a card endpoint
# @cards_bp.route("", methods=["POST"])

# get all cards endppint
# @cards_bp.route("", methods=["GET"])

# get one card by ID endpoint
# @cards_bp.route("/<card_id>", methods=["GET"])

# delete a card endpoint
# @cards_bp.route("/<card_id>", methods=["DELETE"])

# update card endpoint
# @cards_bp.route("/<card_id>", methods=["PUT"])
