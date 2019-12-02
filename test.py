import unittest
import json
from config import config
from app import create_app
from app import db

class TestApi(unittest.TestCase):
    def setUp(self):
        enviroment = config['test']
        self.app = create_app(enviroment)
        self.client = self.app.test_client()
        self.content_type = 'application/json'
        self.path='http://127.0.0.1:5000/api/v1/tasks'

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
    
    def test_one_equals_one(self):
        self.assertEqual(1, 1)

    def test_get_all_tasks(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)
    
    def test_get_first_tas(self):
        new_path = self.path + '/1'
        response =  self.client.get(path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode('utf-8'))
        task_id=data['data']['id']
        self.assertEqual(task_id, 1)
    
    def test_len_tasks(self):
        response =  self.client.get(path=self.path)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(data['data']), 3)
    
    def test_not_found(self):
        new_path = self.path + '/102030'
        response =  self.client.get(path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 404)
    
    def test_create_task(self):
        data = {"title":"Nueva Tarea", "description":"Nueva Description", "deadline":"2019-12-12 12:00:00"}
        response = self.client.post(path=self.path, data=json.dumps(data), content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode('utf-8'))
        task_id = data['data']['id']
        self.assertEqual(task_id, 4)
    
    def test_validate_empty_attribute_title(self):
        data = {"description":"Nueva Description", "deadline":"2019-12-12 12:00:00"}
        response = self.client.post(path=self.path, data=json.dumps(data), content_type=self.content_type)
        self.assertEqual(response.status_code, 400)

    def test_update_task(self):
        new_path = self.path + '/1'
        data = {"title":"Editar titulo"}
        response = self.client.put(path=new_path, data=json.dumps(data), content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

        data_response = json.loads(response.data.decode('utf-8'))
        title = data_response['data']['title']
        self.assertEqual(title, data['title'])

    def test_bad_request_update_task(self):
        new_path = self.path + '/102030'
        data = {"title":"Editar titulo"}
        response =  self.client.put(path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()