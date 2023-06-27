from app import db
from app.models.board import Board
from app.models.card import Card
from flask import Blueprint, request, jsonify, make_response

########## Helper Functions ##########
def validate_model(cls, model_id):
    pass

def create_item(cls):
    pass

def get_all_items(cls):
    pass

def get_item(cls, item_id):
    pass

def update_item(cls, item_id):
    pass

def delete_item(cls, item_id):
    pass

########## Boards Blueprint ##########

boards_bp = Blueprint("boards", __name__, url_prefix="/boards")

@boards_bp.route("", methods=["POST"])
def create_board():
    pass

@boards_bp.route("", methods=["GET"])
def get_all_boards():
    pass

@boards_bp.route("/<board_id>", methods=["GET"])
def get_board(board_id):
    pass

@boards_bp.route("/<board_id>", methods=["DELETE"])
def delete_board(board_id):
    pass

@boards_bp.route("/<board_id>", methods=["PATCH"])
def update_board(board_id):
    pass

@boards_bp.route("/<board_id>/cards", methods=["POST"])
def create_card(board_id):
    pass

@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_all_cards(board_id):
    pass


########## Cards Blueprint ##########

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")

@cards_bp.route("", methods=["GET"])
def get_all_cards():
    pass

@cards_bp.route("/<card_id>", methods=["GET"])
def get_card(card_id):
    pass

@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    pass

@cards_bp.route("/<card_id>", methods=["PATCH"])
def update_card(card_id):
    pass

# @cards_bp.route("/<card_id>/like", methods=["PATCH"])
# def like_card(card_id):
#     pass