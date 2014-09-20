from app import app, db
from models import Todo
from flask import jsonify
from flask import request

@app.route('/')
def index():
  return 'Hello, World!'

@app.route('/api/v1/todos', methods = ['GET'])
def todos():
  return jsonify(todos=[todo.serialize for todo in Todo.query.all()])

@app.route('/api/v1/todos/<int:id>', methods = ['GET'])
def todo(id):
  todo = Todo.query.get(id)
  if todo == None:
    response = jsonify({'code': 404, 'message': 'No Todo found'})
    response.status_code = 404
    return response
  else:
    return jsonify(todo.serialize), 200

@app.route('/api/v1/todos', methods = ['POST'])
def create_todo():
  args = request.args
  todo = Todo(text = args['text'], previous_todo = args['previousTodo'])
  db.session.add(todo)
  db.session.commit()
  response = jsonify(todo.serialize)
  response.status_code = 201
  return response

@app.route('/api/v1/todos/<int:id>', methods = ['PUT'])
def update_todo(id):
  return 'You are updating a todo\n'

@app.route('/api/v1/todos/<int:id>', methods = ['DELETE'])
def delete_todo(id):
  todo = Todo.query.get(id)
  if todo == None:
    response = jsonify({'code': 404, 'message': 'No Todo found'})
  else:
    todo.delete()
    response = jsonify({'code': 200, 'message': 'Todo deleted'})
  return response
