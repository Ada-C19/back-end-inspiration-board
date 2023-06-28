from app import db
from app.models.board import Board
from app.models.card import Card
from flask import Blueprint, request, jsonify, make_response, abort


cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response(
            jsonify({"message": f"{cls.__name__} {model_id} invalid"}), 400))
        
    model = cls.query.get(model_id)
    if not model:
        abort(make_response(
            jsonify({"message": f"{cls.__name__} {model_id} not found"}), 400))
    
    return model 


@cards_bp.route("", methods=["GET"])
def get_all_cards():
    cards = Card.query.all()
    results = [card.to_dict() for card in cards]
    return jsonify(results)

@cards_bp.route("/<card_id>", methods=["GET"])
def get_card(card_id):
    card = validate_model(Card, card_id)
    response_body = {"card": card.to_dict()}
    return response_body

@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):  
    card_to_delete = validate_model(Card, card_id)
    db.session.delete(card_to_delete)
    db.session.commit()
    response_body = {"details": f'Board {card_to_delete.id} "{card_to_delete.title}" succesfully deleted'}
    return response_body

@cards_bp.route("/<card_id>", methods=["PATCH"])
def update_card(card_id):
    card_to_update = validate_model(Card, card_id)
    card_updates = request.json()
    card_to_update.title = card_updates["title"]
    card_to_update.likes_count = card_updates["likes_count"]
    card_to_update.date_created = card_updates["date_created"]
    response_body = {card_to_update.to_dict()}
    db.session.commit()
    return response_body

# @cards_bp.route("/<card_id>/like", methods=["PATCH"])
# def like_card(card_id):
#     pass