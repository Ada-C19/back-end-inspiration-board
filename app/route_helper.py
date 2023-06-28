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
    
        