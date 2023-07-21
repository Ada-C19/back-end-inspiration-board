from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card
import os
import requests


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"details": "Invalid data"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"details": "data not found"}, 404))

    return model


def validate_ids(board_id, card_id):
    board = validate_model(Board, board_id)
    try:
        card_id = int(card_id)
    except:
        abort(make_response({"details": "Invalid card_id"}, 400))
    return board


def post_slack(board_owner, board_title):
    url = "https://slack.com/api/chat.postMessage"
    API_KEY = os.environ.get("SLACK_API_TOKEN_URI")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "channel": "api-test-channel",
        "text": f"{board_owner} just created the board {board_title}"
    }
    response = requests.post(url, headers=headers, data=data)
    return response
