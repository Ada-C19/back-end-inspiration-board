from flask import abort, make_response,request
from app.models.card import Card
from app import db

def validate_model(cls, model_id):
    try: 
        model_id = int(model_id)
    except: 
        abort(make_response({"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

def create_card(request_body, board_id):
    new_card = Card.from_dict(request_body)
    new_card.board_id = board_id

    db.session.add(new_card)
    db.session.commit()
    return new_card.id

def validate_message_length(request_body):
    if len(request_body["message"]) <= 40 and not len(request_body) == 0:
        return
    else:
        abort(make_response({"details": "Message cannot exceed 40 characters"}, 400))
    
def query_sort(board_id):
    sort_param = request.args.get("sort")
    card_query = Card.query.filter(Card.board_id == board_id)

    if sort_param == "asc":
        card_query = card_query.order_by(Card.likes_count)
    if sort_param == "desc":
        card_query = card_query.order_by(Card.likes_count.desc())

    return card_query