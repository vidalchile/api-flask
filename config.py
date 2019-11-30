class Config:
    pass

# Configuraciones para nuestro entorno de desarrollo
class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development' : DevelopmentConfig
}