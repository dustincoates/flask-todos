from app import app, db
from models import Todo
from flask import jsonify, request, render_template

@app.route('/')
def index():
  return render_template('static/app/index.html')

@app.route('/api/v1/todos', methods = ['GET'])
def todos():
  return jsonify(todos=[todo.serialize for todo in Todo.query.all()])

@app.route('/api/v1/todos/<int:id>', methods = ['GET'])
def todo(id):
  todo = Todo.query.get(id)
  if todo == None:
    response = jsonify({'code': 404, 'message': 'No Todo found'})
    return response, 404
  else:
    return jsonify(todo.serialize), 200

@app.route('/api/v1/todos', methods = ['POST'])
def create_todo():
  args = request.args
  todo = Todo(text = args['text'], previous_todo = args['previousTodo'])
  db.session.add(todo)
  db.session.commit()
  response = jsonify(todo.serialize)
  return response, 201

@app.route('/api/v1/todos/<int:id>', methods = ['PUT'])
def update_todo(id):
  todo = Todo.query.get(id)
  if todo == None:
    response = jsonify({'code': 404, 'message': 'No Todo found'})
  else:
    args = request.args
    todo.text = args['text']
    todo.previous_todo = args['previousTodo']
    todo.complete = args['complete']
    db.session.commit()
    response = jsonify(todo.serialize)
    response.status_code = 200
  return response

@app.route('/api/v1/todos/<int:id>', methods = ['DELETE'])
def delete_todo(id):
  todo = Todo.query.get(id)
  if todo == None:
    response = jsonify({'code': 404, 'message': 'No Todo found'})
  else:
    todo.delete()
    response = jsonify({'code': 200, 'message': 'Todo deleted'})
  return response
