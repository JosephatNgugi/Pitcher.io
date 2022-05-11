import os

class Config:
    """Parent class for general configurations settings"""
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLACHEMY_DATABASE_URI = 'postgresql://moringa:Elm1n10@localhost/pitches'
    
class ProdConfig(Config):
    """
    Config Child class for Production configurations 
    Args:
        Config : Parent configurations settings to be inherited
    """
    
    pass

class DevConfig(Config):
    """
    Config child class for Development configuration

    Args:
        Config : Parent configurations settings to be inherited
    """
    DEBUG = True
    
config_options = {
    'developmet': DevConfig,
    'production': ProdConfig
}