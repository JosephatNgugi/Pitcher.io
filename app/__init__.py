from flask import Flask
from config import config_options

# App Initialization
def create_app(config_name):
    app = Flask(__name__)
    
    # Create app config
    app.config.from_object(config_options[config_name])
    
    # Flask extensions Initialization
    from .main import main as main_blueprint
    
    # Blueprint registering
    app.register_blueprint(main_blueprint)
    
    return app