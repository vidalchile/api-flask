from . import db
from sqlalchemy.event  import listen

class Task(db.Model):
    
    # Nombre de la tabla
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    # Nuevo metodo de clase
    @classmethod
    def new(cls, title, description, deadline):
        # Retornara un nuevo objeto tarea
        return Task(title=title, description=description, deadline=deadline)

    # Guardar un objeto
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    # Sobreescribir metodo, retornar el titulo de la tarea
    def __str__(self):
        return self.title
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'deadline': self.deadline
        }

def insert_tasks(*args, **kwargs):
    db.session.add(
        Task(
            title='titulo 1',
            description='descripcion 1',
            deadline='2019-12-12 12:00:00'
        )
    )
    db.session.add(
        Task(
            title='titulo 2',
            description='descripcion 2',
            deadline='2019-12-12 12:00:00'
        )
    )
    db.session.add(
        Task(
            title='titulo 3',
            description='descripcion 3',
            deadline='2019-12-12 12:00:00'
        )
    )
    db.session.commit()

# Despues de que la tabla Task sea creada, ingresamos nuevos registros
listen(Task.__table__, 'after_create', insert_tasks)