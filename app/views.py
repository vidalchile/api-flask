from flask import Blueprint
from flask import jsonify
from .responses import response
from .models.task import Task

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')

@api_v1.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all() # select * from tasks;
    list_tasks = [ task.serialize() for task in tasks]
    return response(list_tasks)

@api_v1.route('/tasks/<id>', methods=['GET'])
def get_task():
    pass

@api_v1.route('/tasks', methods=['POST'])
def create_tasks():
    pass

@api_v1.route('/tasks/<id>', methods=['PUT'])
def update_tasks():
    pass

@api_v1.route('/tasks/<id>', methods=['DELETE'])
def delete_tasks():
    pass


