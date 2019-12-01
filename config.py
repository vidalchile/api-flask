class Config:
    pass

# Configuraciones para nuestro entorno de desarrollo
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/api_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuraciones para nuestro entorno de testing
class TestConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/api_flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'test': TestConfig,
    'development' : DevelopmentConfig
}