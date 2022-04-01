import os
from app.extensions import  db,migrate
from flask import Flask, request
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    configure_app(app, config_class)
    configure_blueprints(app)
    configure_extensions(app)
    return app

def configure_app(app, config_class):
    app.config.from_object(config_class)

def configure_blueprints(app):
    # 注册 blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

def configure_extensions(app):
    '''Configures the extensions.'''
    # Enable CORS
    #cors.init_app(app)
    # Init Flask-SQLAlchemy
    db.init_app(app)
    # Init Flask-Migrate
    migrate.init_app(app, db)
