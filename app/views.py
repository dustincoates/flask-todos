from app import app, db

@app.route('/')
def index():
  return 'Hello, World!'

@app.route('/api/v1/todos', methods = ['GET'])
def todos():
  return "Todo"

@app.route('/api/v1/todos/<int:id>', methods = ['GET'])
def todo(id):
  return 'Single todo\n'

@app.route('/api/v1/todos', methods = ['POST'])
def create_todo():
  return 'You are creating a todo\n'

@app.route('/api/v1/todos/<int:id>', methods = ['PUT'])
def update_todo(id):
  return 'You are updating a todo\n'

@app.route('/api/v1/todos/<int:id>', methods = ['DELETE'])
def delete_todo(id):
  return 'You are deleting a todo\n'
