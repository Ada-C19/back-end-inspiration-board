from flask import Blueprint, jsonify, abort, make_response, request
from flask import Response
from app import db
from app.models.board import Board


board_bp = Blueprint("board_bp", __name__, url_prefix="/board")

def validate_model(cls, id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"{cls.__name__} {id} is invalid"}, 400))
    model = cls.query.get(id)
    if not model:
        abort(make_response({"message":f"{cls.__name__} {id} not found" }, 404))
    
    return model


@board_bp.route('', methods=['POST'])
def create_board():
    request_body = request.get_json()
    try: 
        new_board = Board.from_dict(request_body)
        db.session.add(new_board)
        db.session.commit()
        return make_response(request_body, 201)
    except KeyError:
        details = {"details": "Invalid data"}

        abort(make_response(details, 400))
        
@board_bp.route('', methods=['GET'])
def get_all_boards():
    boards = Board.query.all()
    board_response = []
    for board in boards:
        board_response.append(board.to_dict())
    return jsonify(board_response)

@board_bp.route('/<board_id>', methods=['GET'])
def get_one_board(board_id):
    board = validate_model(Board, board_id)
    response_dict = board.to_dict()
    return response_dict

    
@board_bp.route('/<board_id>', methods = ['PUT'])
def update_board(board_id):
    board = validate_model(Board, board_id)
    request_body = request.get_json()
    board.title = request_body['title']
    board.owner = request_body['owner']
    
    db.session.commit()
    response_dict = board.to_dict()
    return response_dict


@board_bp.route('/<board_id>', methods = ['DELETE'])
def delete_task(board_id):
   board = validate_model(Board,board_id)
   db.session.delete(board)
   db.session.commit()
   return  {
        "details": f'Board {board_id} "{board.title}" successfully deleted'
    }
    
    