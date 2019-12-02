from flask import request
from flask import Blueprint
from flask import jsonify
from .responses import response
from .responses import not_found
from .responses import bad_request
from .models.task import Task

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')

@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    
    # Obtener todos los objetos
    tasks = Task.query.all() # select * from tasks;
    list_tasks = [ task.serialize() for task in tasks]

    return response(list_tasks)

@api_v1.route('/tasks/<id>', methods=['GET'])
def get_task(id):

    # Obtener objeto segun su ID
    task =  Task.query.filter_by(id=id).first()
    
    # Validar existencia objeto
    if task is None:
        return (not_found())
    
    return response(task.serialize())

@api_v1.route('/tasks', methods=['POST'])
def create_tasks():

    # Objeto json que el cliente nos envia
    json  = request.get_json(force=True)

    # Si el cliente no envio el atributo cliente
    if json.get('title') is None or len(json['title']) > 50:
        return bad_request()
    
    if json.get('description') is None:
        return bad_request()

    if json.get('deadline') is None:
        return bad_request()
    
    # Crear nuevo objeto
    new_task = Task.new(json['title'], json['description'], json['deadline'])
    
    # Persistir y guardar objeto
    if new_task.save():
        return response(new_task.serialize())
    
    return bad_request()

@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_tasks(id):
    
    # Obtener objeto
    task = Task.query.filter_by(id=id).first()

    # Validar existencia objeto
    if task is None:
        return (not_found())

    # Obtener json cliente
    json = request.get_json(force=True)

    # Si el cliente no envia un valor para titulos seguira el mismo
    task.title = json.get('title', task.title)
    task.description = json.get('description', task.description)
    task.deadline = json.get('deadline', task.deadline)

    # Persistir cambios
    if task.save():
        return response(task.serialize())

    return bad_request()

@api_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_tasks(id):
    
    task = Task.query.filter_by(id=id).first()

    if task is None:
        return (not_found())

    if task.delete():
        return response(task.serialize())
    
    return bad_request()


