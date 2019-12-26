from marshmallow import Schema
from marshmallow import fields
from marshmallow.validate import Length

class TaskSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'description','deadline')

# Restricciones sobre los parametros
class ParamsTaskSchema(Schema):
    title = fields.Str(required=True, validate=Length(max=50))
    description = fields.Str(required=True, validate=Length(max=200))
    deadline = fields.DateTime(required=True)

# serializar un objeto
task_schema = TaskSchema()

# serializar una lista de objetos
tasks_schema = TaskSchema(many=True)

params_task_schema = ParamsTaskSchema()