from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except: 
        abort(make_response({"details": "Invalid data"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"details": "Data not found"}, 404))

    return model