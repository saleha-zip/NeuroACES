# flaskr/__init__.py
from flask import Flask

from app.config import Config
from .routes import main_bp

def create_app(config_object=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)
    app.register_blueprint(main_bp)
    return app

    