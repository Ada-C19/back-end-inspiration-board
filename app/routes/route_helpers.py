from app import db
from sqlalchemy.exc import DataError
from app.models.board import Board
from app.models.card import Card
from flask import Blueprint, request, jsonify, make_response, abort


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        message = f"'{model_id}' is not a valid id"
        abort(make_response({"error": message}, 400))

    model = cls.query.get(model_id)

    if not model:
        message = f"{cls.__name__} #{model_id} not found"
        abort(make_response({"error": message}, 404))

    return model

def create_item(cls):
    item_data = request.get_json()

    try:
        new_item = cls.from_dict(item_data)
        db.session.add(new_item)
        db.session.commit()
        return make_response({cls.__name__.lower(): new_item.to_dict()}, 201)
    except KeyError as error:
        expected_keys = cls.get_required_fields()
        mising_keys = [key for key in expected_keys if key not in item_data]

        error = 'missing required values'
        error_dict = {"error": error, "details": mising_keys}

        abort(make_response(error_dict, 400))
    except (TypeError, ValueError, DataError) as error_details:
        error = "Invalid request body"
        error_dict = {"error": error, "details": error_details}
        abort (make_response(error_dict, 400))

def get_all_items(cls):
    items = cls.query.all()
    results = [item.to_dict() for item in items]
    return jsonify(results), 200

def get_all_items_with_child(cls, child):
    items = cls.query.all()
    results = [item.to_dict(child) for item in items]
    return jsonify(results), 200

def get_item(cls, item_id):
    item = validate_model(cls, item_id)
    result = {cls.__name__.lower(): item.to_dict()}
    return jsonify(result), 200

def get_item_with_child(cls, item_id, child):
    item = validate_model(cls, item_id)
    result = {cls.__name__.lower(): item.to_dict(child)}
    return jsonify(result), 200

def update_item(cls, item_id):
    item = validate_model(cls, item_id)
    item_data = request.get_json()

    for key, value in item_data.items():
        setattr(item, key, value)

    db.session.commit()
    result = {cls.__name__.lower(): item.to_dict()}

    return jsonify(result), 200

def delete_item(cls, item_id):
    item = validate_model(cls, item_id)

    db.session.delete(item)
    db.session.commit()

    result = {"details": f'{cls.__name__} #{item.id} successfully deleted'}
    return make_response(result, 200)

def update_likes(cls, item_id, change):
    item = validate_model(cls, item_id)
    item.likes_count += change
    db.session.commit()
    result = {cls.__name__.lower(): item.to_dict()}

    return jsonify(result), 200