class Config:
    pass

# Configuraciones para nuestro entorno de desarrollo
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/api_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development' : DevelopmentConfig
}