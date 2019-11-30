from flask import Flask

app = Flask(__name__)

def create_app():
    # Retornar instancia para levantar nuestro servidor
    return app