from flask import Blueprint
from flask import request
from flask import jsonify
from flask import Response
from flask import make_response
from app import db


board_bp = Blueprint("board_bp", __name__, url_prefix="/board")