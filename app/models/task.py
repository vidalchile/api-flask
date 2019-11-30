from . import db

class Task(db.Model):
    
    # Nombre de la tabla
    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    # Sobreescribir metodo, retornar el titulo de la tarea
    def __str__(self):
        return self.title