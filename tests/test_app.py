import unittest
from app.app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Configura um cliente de teste do Flask antes de cada teste
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # Testa se a rota principal (/) retorna 200 OK
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_status_endpoint(self):
        # Testa se a rota /status retorna a palavra "OK"
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'OK', response.data)

if __name__ == '__main__':
    unittest.main()