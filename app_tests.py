import os
import app
import unittest
import tempfile
import mock
from flask.ext.sqlalchemy import SQLAlchemy
from app.models import Todo

class FlaskrTestCase(unittest.TestCase):

  def setUp(self):
    self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True
    self.app = app.app.test_client()

  def tearDown(self):
    os.close(self.db_fd)
    os.unlink(app.app.config['DATABASE'])
    
  
  def test_home(self):
    res = self.app.get('/')
    assert 'Hello, World!' in res.data

  def test_api_index(self):
    res = self.app.get('/api/v1/todos')
    self.assertEqual(res.status_code, 200)
    
  def test_api_show_with_no_todo(self):
    Todo.query.delete()
    res = self.app.get('/api/v1/todos/1')
    self.assertEqual(res.status_code, 404)
    
  def test_api_show_with_todo(self):
    todo = Todo(text = "Something to do", previous_todo = 12)
    res = self.app.get('/api/v1/todos/1')
    self.assertEqual(res.status_code, 200)
    Todo.query.delete()
    
  def test_api_create_with_correct_params(self):
    data = {'text': 'Something to do', 'previousTodo': 2}
    res = self.app.post('/api/v1/todos?text=Something+to+do&previousTodo=2', 
      headers = {'content-type':'application/json'})
    self.assertEqual(res.status_code, 200)
    
  def test_api_update(self):
    res = self.app.put('/api/v1/todos/1')
    self.assertEqual(res.status_code, 200)
    
  def test_api_delete(self):
    res = self.app.delete('/api/v1/todos/1')
    self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
  unittest.main()