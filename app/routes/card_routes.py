from flask import Blueprint, request, jsonify, make_response
from app import db

# example_bp = Blueprint('example_bp', __name__)
bp = Blueprint("cards", __name__, url_prefix="/cards")

# Read all cards:


@card_bp.route("", methods=["Get"])
def get_all_cards():
    pass
