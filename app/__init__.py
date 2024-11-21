from flask import Flask
from .extensions import db, migrate
from .routes import register_routes
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    register_routes(app)

    return app
