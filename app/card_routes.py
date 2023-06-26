from flask import Blueprint, request, jsonify, make_response
from app import db

card_bp = Blueprint('card_bp', __name__, url_prefix="/cards")