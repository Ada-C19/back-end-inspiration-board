from app import db
from flask import Blueprint, request, jsonify, make_response
from app.models.board import Board
from app.models.card import Card

bp = Blueprint('boards', __name__, url_prefix="/boards")
