from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card

# example_bp = Blueprint('example_bp', __name__)
card_bp = Blueprint("cards", __name__, url_prefix="/cards")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{model_id} is not a vlid type ({type(model_id)})"}))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} does not exist"}, 404))

    return model    


@card_bp.route("", methods=["POST"])
def create_card():
    request_body = request.get_json()

    new_card = Card.from_dict(request_body)

    db.session.add(new_card)
    db.session.commit()

    return jsonify(new_card.to_dict()), 201


@card_bp.route("", methods=["GET"])
def read_all_cards():
    board_query = request.args.get("board")

    if board_query:
        cards = Card.query.filter_by(board=board_query)

    cards_response = []

    for card in cards:
        cards_response.append(card.to_dict())

    return jsonify(cards_response)


@card_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    card = validate_model(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return make_response(f"Card #{card_id} successfully deleted")