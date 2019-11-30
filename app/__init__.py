from flask import Flask
from .models import db 
from .models.task import Task
from .views import api_v1

app = Flask(__name__)

def create_app(enviroment):
    
    # Configuraciones del proyecto
    app.config.from_object(enviroment)

    # Registrar nuestras urls
    app.register_blueprint(api_v1)

    # Crear todos los modelos / tablas
    with app.app_context():
        db.init_app(app)
        db.create_all()

    # Retornar instancia para levantar nuestro servidor
    return app