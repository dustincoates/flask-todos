from app import db

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  complete = db.Column(db.Boolean, default = False, nullable = False)
  text = db.Column(db.String(256), nullable = False)
  position = db.Column(db.Integer, nullable = False, unique = True)
