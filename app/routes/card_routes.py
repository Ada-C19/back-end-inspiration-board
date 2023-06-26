from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.models.card import Card
from .routes_helper import validate, validate_card


cards_bp = Blueprint("card_bp", __name__, url_prefix="/cards")


# @cards_bp.route("", methods=["POST"])
# def create_card():
#     request_body = request.get_json()
#     if "board_id" not in request_body or "message" not in request_body:
#         return make_response({"details": "data not in request body"}, 400)

#     try:
#         board_id = request_body["board_id"]
#         validate(Board, board_id)
#         new_card = Card.from_dict(request_body)
#         validate_card(new_card)
#     except:
#         return jsonify({"details": "Invalid Data"}), 400

#     db.session.add(new_card)
#     db.session.commit()
#     return {
#         "card": {
#             "id": new_card.card_id,
#             "message": new_card.message,
#             "board_id": new_card.board_id
#         }
#     }, 201



# @cards_bp.route("", methods=["GET"])
# def get_all_cards():

# #     cards = Card.query.all()
# #     cards_response = [card.to_dict() for card in cards]

# #     return jsonify(cards_response), 200


# # @ cards_bp.route("/<obj_id>", methods=["GET"])
# # def get_one_card(obj_id):
# #     card = validate(Card, obj_id)

# #     return jsonify({"card": card.to_dict()})