from app import app, db
from models import Todo
from flask import jsonify

@app.route('/')
def index():
  return 'Hello, World!'

@app.route('/api/v1/todos', methods = ['GET'])
def todos():
  return "Todo"

@app.route('/api/v1/todos/<int:id>', methods = ['GET'])
def todo(id):
  todo = Todo.query.get(id)
  if todo == None:
    response = jsonify({'code': 404, 'message': 'No Todo found'})
    response.status_code = 404
    return response
  else:
    return "Success"

@app.route('/api/v1/todos', methods = ['POST'])
def create_todo():
  return 'You are creating a todo\n'

@app.route('/api/v1/todos/<int:id>', methods = ['PUT'])
def update_todo(id):
  return 'You are updating a todo\n'

@app.route('/api/v1/todos/<int:id>', methods = ['DELETE'])
def delete_todo(id):
  return 'You are deleting a todo\n'
