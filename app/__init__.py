from os import makedirs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import click

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_file=None):
    # Create and configure the app
    app = Flask(__name__)
    if config_file:
        app.config.from_pyfile(config_file)
    else:
        app.config.from_envvar('APPLICATION_SETTINGS')
    
    # Ensure the instance folder exists
    try:
        makedirs(app.instance_path)
    except OSError:
        pass
    
    
    # Inintialize Flask extensions
    initialize_extensions(app=app)
    
    # Register Blueprints
    register_blueprint(app)
    
    return app 


def register_blueprint(app):
    from app.blueprints import index_bp
    from app.blueprints import auth_bp
    from app.blueprints import profile_bp
    
    app.register_blueprint(index_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(auth_bp)
    

def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    
    # Flask-Login configuration
    login_manager.init_app(app)
    
    # SQLAlchemy configuration
    db.init_app(app)
    with app.app_context():
        app.cli.add_command(init_db)
        
    
@click.command('init-db')
def init_db():
    '''
    Usage: $> Flask init-db 
    Drop all tables if any exists and create new tables.
    '''
    
    inspector = db.inspect(db.engine)
    tables = inspector.get_table_names()
    if len(tables) > 0:
        print('\n-=-=-=-=-\nDropping all existing tables.')
        db.drop_all()
    print('-=-=-=-=-\nCreating tables.\n-=-=-=-=-\n')
    db.create_all()