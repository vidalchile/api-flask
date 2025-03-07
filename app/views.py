from flask import request
from flask import Blueprint
from flask import jsonify
from .responses import response
from .responses import not_found
from .responses import bad_request
from .models.task import Task
from .schemas import task_schema, tasks_schema, params_task_schema

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')

def funcion_a(function_b):
    def funcion_c(*args, **kwargs):
        # Si el parametro ID no existe retornaremos 0
        id = kwargs.get('id',0);
        # Obtener la tarea
        task = Task.query.filter_by(id=id).first();
        if task is None:
            return not_found()
        return function_b(task)
    # Para que el decorador pueda ser utilizado por distintas funciones (renombrar funcion)
    funcion_c.__name__ = function_b.__name__
    return funcion_c

@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    
    # Obtener pagina actual
    actual_page = int(request.args.get('page', 1))
    
    # Ordenar registros
    order = request.args.get('order', 'desc')

    # Obtener datos paginados
    tasks = Task.get_by_page(order, actual_page)
    
    # Obtener todos los objetos
    # tasks = Task.query.all() # select * from tasks;
    
    # list_tasks = [ task_schema.dump(task) for task in tasks]
    return response(tasks_schema.dump(tasks))

@api_v1.route('/tasks/<id>', methods=['GET'])
@funcion_a
def get_task(task):
    return response(task_schema.dump(task))

@api_v1.route('/tasks', methods=['POST'])
def create_tasks():

    # Objeto json que el cliente nos envia
    json  = request.get_json(force=True)
    error = params_task_schema.validate(json)
    if error:
        print(error)
        return bad_request(error)

    # Si el cliente no envio el atributo cliente
    #if json.get('title') is None or len(json['title']) > 50:
    #    return bad_request()
    
    #if json.get('description') is None:
    #    return bad_request()

    #if json.get('deadline') is None:
    #    return bad_request()
    
    # Crear nuevo objeto
    new_task = Task.new(json['title'], json['description'], json['deadline'])
    
    # Persistir y guardar objeto
    if new_task.save():
        return response(task_schema.dump(new_task))
    
    return bad_request()

@api_v1.route('/tasks/<id>', methods=['PUT'])
@funcion_a
def update_tasks(task):
    # Obtener json cliente
    json = request.get_json(force=True)

    # Si el cliente no envia un valor para titulos seguira el mismo
    task.title = json.get('title', task.title)
    task.description = json.get('description', task.description)
    task.deadline = json.get('deadline', task.deadline)

    # Persistir cambios
    if task.save():
        return response(task_schema.dump(task))

    return bad_request()

@api_v1.route('/tasks/<id>', methods=['DELETE'])
@funcion_a
def delete_tasks(task):
    if task.delete():
        return response(task_schema.dump(task))
    return bad_request()


