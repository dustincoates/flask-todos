from app import db

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  complete = db.Column(db.Boolean, default = False, nullable = False)
  text = db.Column(db.String(256), nullable = False)
  previous_todo = db.Column(db.Integer)
  
  
  
  @property
  def serialize(self):
    """Serialize the Todo for JSON"""
    return {
      'id': self.id,
      'text': self.text,
      'previousTodo': self.previous_todo
    }