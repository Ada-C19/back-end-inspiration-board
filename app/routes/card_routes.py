from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card
from app.models.board import Board
from app.routes.board_routes import board_bp


card_bp = Blueprint("cards", __name__, url_prefix="/cards")
### Validate model ###
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{model_id} is not a vlid type ({type(model_id)})"}))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} does not exist"}, 404))

    return model    


### Post a new card under a board ###
@board_bp.route("/<board_id>/cards", methods = ["POST"])
def create_card_by_board_id(board_id):

    board = validate_model(Board, board_id)

    request_body = request.get_json()

    new_card = Card(
        message=request_body["message"],
        liked_count=request_body["liked_count"],
        board=board
    )

    db.session.add(new_card)
    db.session.commit()

    return jsonify(f"Card {new_card.card_id} under {new_card.board.title} was successfully created."), 201


### Get all cards from a board ###
@board_bp.route("/<board_id>/cards", methods=["GET"])
def get_all_cards_with_board_id(board_id):
    board = validate_model(Board, board_id)

    card_response = []

    for card in board.cards:
        card_response.append(card.to_dict())

    return jsonify(card_response),200


### Update liked_count by card ###
@card_bp.route('/<card_id>', methods=['PATCH'])
def update_liked_count(card_id):
    card = validate_model(Card, card_id)

    if not card.liked_count:
        card.liked_count = 0

    card.liked_count = card.liked_count + 1

    db.session.commit()

    return card.to_dict(), 200


### Delete card ###
@card_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = validate_model(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return make_response(f"Card #{card_id} successfully deleted")


