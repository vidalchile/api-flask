from flask import Flask

app = Flask(__name__)

def create_app(enviroment):
    
    # Configuraciones del proyecto
    app.config.from_object(enviroment)

    # Retornar instancia para levantar nuestro servidor
    return app