from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.board import Card

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint("boards", __name__, url_prefix = "/boards")

#####   ---   BOARD ROUTES   -   #####
#  GET - Read ALL boards
@board_bp.route("", methods = ["GET"])
def read_all_boards():
    boards_response = []                # initialize list to hold all boards returned
    boards = boards.query.all()         # call to get all boards

    # calls make_board_dict helper function to populate Board class attributes for each board and appends to the list
    boards_response = [make_board_dict(board)for board in boards]       

    return jsonify(boards_response)     # returns jsonify response 

# GET - Read ONE board
def read_board():
    board = board.query.all


#####   ---   HELPER FUNCTIONS   -   #####

# Validate Model ID 
# Takes: Model Class Name, Class Infor from query
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        abort(make_response({"message": f"{model_id} is not a valid type. A {(type(model_id))} data type was provided. Must be a valid integer data type."},400))
    
    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message" : f"{cls.__name__} {model_id} does not exist"},404))
    
    return model


# Make Board into Dictionary
# note: eventually move to Board Class
#       Takes: board object from query
#       Returns: board dictionary
def make_board_dict(board):
    return dict(
        title = board.title,
        owner = board.owner)
