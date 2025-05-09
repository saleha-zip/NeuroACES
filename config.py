# config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base config with defaults. Extend this for all environments."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-want-to-override-this')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///' + os.path.join(basedir, 'app.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Any other common settings:
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)

class DevelopmentConfig(Config):
    DEBUG = True
    # You might use a local SQLite dev database:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')

class TestingConfig(Config):
    TESTING = True
    # Use an in-memory database for fast tests:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False  # often turned off in tests

class ProductionConfig(Config):
    DEBUG = False
    # Production should supply a real DATABASE_URL env var:
    # e.g. postgresql://user:pass@host/dbname