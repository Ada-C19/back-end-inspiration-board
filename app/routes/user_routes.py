from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.user import User

user_bp = Blueprint("user", __name__, url_prefix="/user")

@user_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return make_response(jsonify({"message": "Username and password are required."}), 400)

    user = User.query.filter_by(username=username).first()

    if not user or user.password != password:
        return make_response(jsonify({"message": "Invalid username or password."}), 401)

    return jsonify({"message": "Login successful.", "user": user.to_dict()}), 200


@user_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    first_name = data.get("firstName")
    last_name = data.get("lastName")

    if not username or not password or not first_name or not last_name:
        return make_response(jsonify({"message": "Username, password, first name, and last name are required."}), 400)

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return make_response(jsonify({"message": "Username already taken."}), 409)

    new_user = User(username=username, password=password, first_name=first_name, last_name=last_name)
    db.session.add(new_user)
    db.session.commit()

    return new_user.to_dict(), 201


