
"""
Copyright (c) 2024 Shardul Rajesh Khare, Shruti Dhond, Pranav Manbhekar
This code is licensed under MIT license (see LICENSE for details)

@author: Burnout


This python file is used in and is part of the Burnout project.

For more information about the Burnout project, visit:
https://github.com/SEFall24-Team61/FitnessAppNew

"""
import unittest
import os,sys,inspect
import json
from application import app
from flask import session
from unittest.mock import patch, MagicMock
from unittest import TestCase
from datetime import datetime
import numpy as np
from bson.objectid import ObjectId, InvalidId 

class TestApplication(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_reminders(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/reminders')
            self.assertEqual(response.status_code, 200)
    
    def test_reminders_route_no_session(self):
        with self.app as client:
            response = client.get('/reminders', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Log In', response.data)  # Ensure redirection to the login page

    @patch("application.mongo.db.reminders.insert_one")
    def test_create_workout_reminder(self, mock_insert_one):
        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"

            form_data = {
                "reminder_type": "workout",
                "workout_title": "Morning Yoga",
                "notes": "Don't forget to stay hydrated.",
            }
            response = client.post("/reminders", data=form_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)

    @patch("application.mongo.db.reminders.insert_one")
    def test_create_goal_reminder(self, mock_insert_one):
        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"

            form_data = {
                "reminder_type": "goal",
                "goal_weight": "65",
                "notes": "Achieve by December!",
            }
            response = client.post("/reminders", data=form_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
    
    def test_reminders_get_no_session(self):
        """Test accessing the reminders page without login."""
        response = self.app.get('/reminders', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log In', response.data)  # Assuming redirection to login page

  
    def test_reminder_history_no_session(self):
        """Test accessing the reminder history without login."""
        response = self.app.get('/reminder_history', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log In', response.data)  # Assuming redirection to login page

    def test_reminders_post_missing_fields(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            # POST without necessary fields
            form_data = {
                'reminder_type': 'goal',
                'notes': 'Missing goal weight'
            }
            response = client.post('/reminders', data=form_data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_reminders_valid(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            form_data = {
                'set_date': '2024-11-23',  
                'reminder_type': 'goal',
                'goal_weight': '60',
                'workout_title': None,
                'notes': ''
            }

            response = client.post('/reminders', data=form_data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)


    def test_reminders_invalid_small_goal(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            form_data = {
                'set_date': '2024-11-23',  
                'reminder_type': 'goal',
                'goal_weight': '-1',
                'workout_title': None,
                'notes': ''
            }

            response = client.post('/reminders', data=form_data, follow_redirects=True)
            with open("request.txt", "w") as f:
                f.write(str(response.data))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Goal Weight must be between 0 and 500 kg', response.data) 


    def test_reminders_invalid_big_goal(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            form_data = {
                'set_date': '2024-11-23',  
                'reminder_type': 'goal',
                'goal_weight': '501',
                'workout_title': None,
                'notes': ''
            }

            response = client.post('/reminders', data=form_data, follow_redirects=True)
            with open("request.txt", "w") as f:
                f.write(str(response.data))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Goal Weight must be between 0 and 500 kg', response.data) 
        

    def test_reminders_invalid_remindertype(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            form_data = {
                'set_date': '2024-11-23',  
                'reminder_type': 'Invalid Type',
                'goal_weight': '501',
                'workout_title': None,
                'notes': ''
            }

            response = client.post('/reminders', data=form_data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_reminders_post_missing_required_fields(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            form_data = {
                'set_date': '',  # Missing date
                'reminder_type': 'goal',
                'goal_weight': '',
                    'notes': ''
            }

            response = client.post('/reminders', data=form_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            msg = str(datetime.now().strftime('%Y-%m-%d')).encode('utf-8')
            self.assertIn(msg, response.data)  # Update message as per actual validation

    def test_reminders_post_invalid_date(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            form_data = {
                'set_date': '1111-11-11',  # Missing date
                'reminder_type': 'goal',
                'goal_weight': '',
                    'notes': ''
            }

            response = client.post('/reminders', data=form_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            msg = str(datetime.now().strftime('%Y-%m-%d')).encode('utf-8')
            self.assertIn(msg, response.data)  # Update message as per actual validation

    def test_reminders_post_null_note(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            form_data = {
                'set_date': '2024-11-23',
                'reminder_type': 'invalid_type',
                'goal_weight': '65',
                'notes': ''
            }

            response = client.post('/reminders', data=form_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)

    def test_reminder_history_get_valid_user(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'

            response = client.get('/reminder_history')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Reminder History', response.data)

    def test_reminder_history_get_no_session(self):
        with self.app as client:
            response = client.get('/reminder_history', follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Log In', response.data)

    def test_goal_progress_half_completion(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            goal_data = {
                'original_weight': 100,
                'latest_weight': 75,
                'goal_weight': 50,
                'progress': 50,
            }
            response = client.get('/dashboard', data=goal_data, follow_redirects=True)
            
            self.assertEqual(response.status_code, 200)
            with open("request.txt", "w") as f:
                f.write(str(response.data))
            self.assertIn(b'50% Goal Achieved', response.data)


    

if __name__ == '__main__':
    unittest.main()
