import unittest
from application import app
from flask import session

class TestApplication(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  # Expect a redirect status code

    def test_login_route(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)  # Expect a success status code

    def test_register_route(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)  # Expect a success status code

    def test_calories_route(self):
        # Assuming the user is logged in (session is set)
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/calories')
            self.assertEqual(response.status_code, 200)  # Expect a success status code

    def test_display_profile_route(self):
        # Assuming the user is logged in (session is set)
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/display_profile')
            self.assertEqual(response.status_code, 200)  # Expect a success status code

    def test_user_profile_route(self):
        # Assuming the user is logged in (session is set)
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/user_profile')
            self.assertEqual(response.status_code, 200)  # Expect a success status code

    def test_history_route(self):
        # Assuming the user is logged in (session is set)
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/history')
            self.assertEqual(response.status_code, 200)  # Expect a success status code

if __name__ == '__main__':
    unittest.main()
