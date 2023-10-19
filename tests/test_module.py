import unittest
from your_flask_app import app

class TestLoginRoute(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_login_route_status_code(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

if _name_ == '_main_':
    unittest.main()