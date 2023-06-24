from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.board import Card


cards_bp = Blueprint("cards", __name__, url_prefix="/cards")
@cards_bp.routes("", methods=["POST"])
