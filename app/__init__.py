from flask import Flask
from .models import db 
from .models.task import Task

app = Flask(__name__)

def create_app(enviroment):
    
    # Configuraciones del proyecto
    app.config.from_object(enviroment)

    # Crear todos los modelos / tablas
    with app.app_context():
        db.init_app(app)
        db.create_all()

    # Retornar instancia para levantar nuestro servidor
    return app