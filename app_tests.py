import os
import app
import unittest
import tempfile
from flask.ext.sqlalchemy import SQLAlchemy

class FlaskrTestCase(unittest.TestCase):

  def setUp(self):
    self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True
    self.app = app.app.test_client()
    db = SQLAlchemy(app.app)

  def tearDown(self):
    os.close(self.db_fd)
    os.unlink(app.app.config['DATABASE'])
    pass
  
  def test_home(self):
    res = self.app.get('/')
    assert 'Hello, World!' in res.data

  def test_api_index(self):
    res = self.app.get('/api/v1/todos')
    self.assertEqual(res.status_code, 200)
    
  def test_api_show(self):
    res = self.app.get('/api/v1/todos/1')
    self.assertEqual(res.status_code, 200)
    
  def test_api_create(self):
    res = self.app.post('/api/v1/todos')
    self.assertEqual(res.status_code, 200)
    
  def test_api_update(self):
    res = self.app.put('/api/v1/todos/1')
    self.assertEqual(res.status_code, 200)
    
  def test_api_delete(self):
    res = self.app.delete('/api/v1/todos/1')
    self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
  unittest.main()