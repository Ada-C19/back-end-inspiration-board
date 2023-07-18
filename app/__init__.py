from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS
from app.routes.user_routes import user_bp

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    CORS(app)
    app.config["CORS_HEADERS"] = "Content-Type"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    # from .routes import example_bp
    from app.routes.board_routes import board_bp
    from app.routes.card_routes import card_bp

    app.register_blueprint(board_bp)
    app.register_blueprint(card_bp)
    app.register_blueprint(user_bp)

    # app.register_blueprint(example_bp)

    from app.models.card import Card
    from app.models.board import Board 
    
    return app
