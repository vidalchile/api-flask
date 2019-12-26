from marshmallow import Schema

class TaskSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'description','deadline')

# serializar un objeto
task_schema = TaskSchema()

# serializar una lista de objetos
tasks_schema = TaskSchema(many=True)