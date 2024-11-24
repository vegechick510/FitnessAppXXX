
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

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  

    def test_login_route(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)  

    def test_register_route(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)  

    def test_calories_route(self):
        
        response = self.app.get('/calories')
        self.assertEqual(response.status_code, 302)  

    def test_user_profile_route(self):
        
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/user_profile')
            self.assertEqual(response.status_code, 200)  

    def test_history_route(self):
        
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/history')
    
            self.assertEqual(response.status_code, 200)  
    def test_bmi_calci_post(self):
        response = self.app.post('/bmi_calc', data={'weight': 70, 'height': 175})
        self.assertEqual(response.status_code, 200)

    def test_ajaxsendrequest_route(self):
    
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.post('/ajaxsendrequest', data={'receiver': 'friend@example.com'})
            self.assertEqual(response.status_code, 200)  

    def test_ajaxcancelrequest_route(self):
        
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.post('/ajaxcancelrequest', data={'receiver': 'friend@example.com'})
            self.assertEqual(response.status_code, 200)  

    def test_ajaxapproverequest_route(self):
        
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.post('/ajaxapproverequest', data={'receiver': 'friend@example.com'})
            self.assertEqual(response.status_code, 200) 
   
    def test_dashboard_route(self):
    
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/dashboard')
            self.assertEqual(response.status_code, 200)  

    def test_add_favorite_route(self):
        
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.post('/add_favorite', json={'exercise_id': '123', 'action': 'add'})
            self.assertEqual(response.status_code, 200)  

    def test_favorites_route(self):
        
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/favorites')
            self.assertEqual(response.status_code, 200)  

    def test_exercise_routes(self):
        
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'

            exercise_routes = ['/yoga', '/swim', '/abbs', '/belly', '/core', '/gym', '/walk', '/dance', '/hrx']

            for route in exercise_routes:
                response = client.get(route)
                self.assertEqual(response.status_code, 200)  

    @patch("application.mongo.db.profile.find_one")
    @patch("application.mongo.db.profile.update_one")
    def test_submit_reviews_route(self, mock_update_one, mock_find_one):
        # Mock find_one to return a valid student profile with a coach
        mock_find_one.return_value = {
            "email": "testuser@example.com",
            "user_type": "student",
            "coach": "Coach1"  # Ensures that 'coach' is present
        }
        
        mock_update_one.return_value = MagicMock()

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            response = client.get('/submit_review', follow_redirects=True)
            
            self.assertEqual(response.status_code, 200)
            

    # @patch('application.mongo.db.profile.find_one')
    # def test_display_profile_route(self, mock_find_one):
    #     mock_find_one.return_value = {'target_weight': 70.0}

    #     with self.app as client:
    #         with client.session_transaction() as sess:
    #             sess['email'] = 'testuser@example.com'

    #         response = client.post('/display_profile')
    #         self.assertEqual(response.status_code, 200)

    def test_community_route(self):
    
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/community')
            self.assertEqual(response.status_code, 200)


    def test_delete_friend_route(self):
    
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/delete_friend')
            self.assertEqual(response.status_code, 302)


    def test_display_beginner_workout_recommendation(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/beginner')
            self.assertEqual(response.status_code, 200)


    def test_post_beginner_workout_recommendation(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.post('/beginner', data={'selectedPrimaryMuscle': 'Chest'})

            self.assertEqual(response.status_code, 302)
            self.assertIn('selectedPrimaryMuscle', response.headers['Set-Cookie'])
            self.assertIn('Chest', response.headers['Set-Cookie'])
            self.assertEqual(response.location, 'http://localhost/recommend')


    def test_display_advanced_workout_recommendation(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/advanced')
            self.assertEqual(response.status_code, 200)


    def test_post_advanced_workout_recommendation(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.post('/advanced', data={'selectedPrimaryMuscle': 'Chest'})

            self.assertEqual(response.status_code, 302)
            self.assertIn('selectedPrimaryMuscle', response.headers['Set-Cookie'])
            self.assertIn('Chest', response.headers['Set-Cookie'])
            self.assertEqual(response.location, 'http://localhost/recommend')


    def test_display_recommend_workout_route(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/recommend_workout')
            self.assertEqual(response.status_code, 200)


    def test_beginner_routing_recommend_workout(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.post('/recommend_workout', data={'selectedLevel': 'Beginner'})
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, 'http://localhost/beginner')


    def test_advanced_routing_recommend_workout_route(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.post('/recommend_workout', data={'selectedLevel': 'Advanced'})
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, 'http://localhost/advanced')
            

    @patch('application.collection')  # Mock the MongoDB collection
    @patch('application.tfidf_vectorizer')  # Mock the TF-IDF vectorizer
    @patch('application.linear_kernel')  # Mock the linear_kernel function
    def test_recommend_exercises(self, mock_linear_kernel, mock_tfidf_vectorizer, mock_collection):
        # Mock the TF-IDF transformation and linear kernel computation
        mock_tfidf_vectorizer.transform.return_value = MagicMock()  # Mock the result of transform
        mock_linear_kernel.return_value = np.array([[0.1, 0.2, 0.3, 0.4, 0.5]])  # Mock cosine similarity scores

        # Mock the MongoDB find_one method to return sample exercise data
        mock_collection.find_one.side_effect = lambda query: {
            "id": query["id"],
            "instructions": "Do this exercise.,",
            "name": "Sample Exercise"
        }

        # Set up cookies and form data for the POST request
        with self.app as client:
            # Set a cookie for the primary muscle
            client.set_cookie('localhost', 'selectedPrimaryMuscle', 'chest')

            # Simulate form data
            form_data = {
                'level': '1',
                'equipment': 'dumbbell',
                'force': 'push',
                'mechanic': 'isolation',
                'category': 'strength',
                'secondaryMuscles[]': ['triceps', 'shoulders']
            }

            # Perform the POST request
            response = client.post('/recommend', data=form_data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Sample Exercise', response.data)

    
    @patch('application.collection.find_one')  # Mock the MongoDB collection find_one method
    @patch('application.tfidf_vectorizer.transform')  # Mock TF-IDF vectorizer transform
    @patch('application.cosine_similarity')  # Mock cosine similarity function
    def test_more_recommendations_post(self, mock_cosine_similarity, mock_tfidf_transform, mock_find_one):
        mock_tfidf_transform.return_value = "mock_tfidf_matrix"  # Mock output of the TF-IDF transformation
        mock_cosine_similarity.return_value = np.array([[0.9, 0.8, 0.7, 0.6, 0.5]])  # Mock similarity scores
        mock_find_one.side_effect = [
            {"id": "1", "instructions": "Instruction 1."},
            {"id": "2", "instructions": "Instruction 2."},
            {"id": "3", "instructions": "Instruction 3."},
            {"id": "4", "instructions": "Instruction 4."},
            {"id": "5", "instructions": "Instruction 5."}
        ]

        with self.app as client:
            with client.session_transaction() as sess:
                sess['selectedPrimaryMuscle'] = 'Chest'
            
            # Simulate a POST request with user input
            user_input = {
                'level': ['Beginner'],
                'equipment': ['Dumbbell'],
                'force': ['Push'],
                'mechanic': ['Compound'],
                'category': ['Strength']
            }
            response = client.post('/more_recommendations',
                                    data={
                                        'user_input': json.dumps(user_input),
                                        'secondaryMuscles[]': ['Triceps', 'Shoulders']
                                    })

            self.assertEqual(response.status_code, 200)


    def test_more_recommendations_get(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/more_recommendations')
            self.assertEqual(response.status_code, 200)

    def test_progress_monitor(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/progress_monitor')
            self.assertEqual(response.status_code, 200)
    
    def test_progress_monitor_post_valid_data(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            form_data = {
                'current_weight': '70',
                'goal_weight': '65',
                'waist': '30',
                'hips': '35',
                'chest': '40',
                'notes': 'Good progress!'
            }

            response = client.post('/progress_monitor', data=form_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)

    def test_progress_monitor_post_missing_fields(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            form_data = {
                'current_weight': '',  
                'goal_weight': '65',
                'waist': '30',
                'hips': '75',
                'chest': '75',
                'notes': 'Waist measurements not within range'
            }

            response = client.post('/progress_monitor', data=form_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Waist must be between 50 and 150 ', response.data) 
    
    def test_progress_monitor_post_missing_fields(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            form_data = {
                'current_weight': '',  
                'goal_weight': '65',
                'waist': '75',
                'hips': '30',
                'chest': '75',
                'notes': 'Hips measurements not within range'
            }

            response = client.post('/progress_monitor', data=form_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Hips must be between 70 and 160 cm', response.data) 

    def test_progress_monitor_post_missing_fields(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            form_data = {
                'current_weight': '',  
                'goal_weight': '65',
                'waist': '75',
                'hips': '75',
                'chest': '30',
                'notes': 'Hips measurements not within range'
            }

            response = client.post('/progress_monitor', data=form_data, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Chest must be between 70 and 150 cm', response.data) 

    

    def test_progress_history(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/progress_history')
            self.assertEqual(response.status_code, 200)

    def test_progress_history_get_no_session(self):
        with self.app as client:
            response = client.get('/progress_history', follow_redirects=True)
            
            self.assertEqual(response.status_code, 200)  
    
    def test_progress_history_post_request(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            response = client.post('/progress_history', follow_redirects=True)

            self.assertEqual(response.status_code, 405)  
    
    @patch('application.collection')
    def test_progress_history_no_entries(self, mock_db):
        """Test the /progress_history page when there are no entries for the user."""
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            # Mock an empty response from the database
            mock_db.db.progress.find.return_value = []
            
            response = client.get('/progress_history')
            self.assertEqual(response.status_code, 200)

    def test_progress_history_redirect_logged_out(self):
        """Test that a logged-out user is redirected to the home page when accessing /progress_history."""
        with self.app as client:
            response = client.get('/progress_history', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            #self.assertIn(b'Unauthorized access.', response.data)  # Check if redirected to the login page

    def test_wellness_log(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/wellness_log')
            self.assertEqual(response.status_code, 200)

    def test_update_streak(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            response = client.get('/update_streak')
            self.assertEqual(response.status_code, 200)
    
    def test_update_streak_no_session(self):
        with self.app as client:
            response = client.get('/update_streak', follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Log In', response.data)  

    def test_update_streak_no_session(self):
        with self.app as client:
            response = client.get('/update_strea', follow_redirects=True)

            self.assertEqual(response.status_code, 404)

    @patch('application.collection')
    def test_update_streak_get_with_session(self, mock_db):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'
            
            mock_db.db.streaks.insert_one({
                'email': 'testuser@example.com',
                'date': '2020-01-01',
                'streak': 3
            })

            response = client.get('/update_streak')
            self.assertEqual(response.status_code, 200)

    @patch("application.mongo.db.user.find_one")
    @patch("application.mongo.db.user.find")
    @patch("application.mongo.db.form_reviews.find")
    @patch("application.mongo.db.reminders.find")
    @patch("application.mongo.db.meetings.find")
    def test_coach_dashboard_negative(self, mock_meetings_find, mock_reminders_find, mock_form_reviews_find, mock_user_find, mock_user_find_one):
        # No mock return values are needed since we are testing a failure scenario
        mock_user_find_one.return_value = None  # Simulate no coach data found
        
        with self.app as client:
            response = client.get('/coach_dashboard')
            self.assertNotIn(b"Coach Dashboard", response.data)
            self.assertEqual(response.status_code, 302)

    def test_submit_feedback_without_login(self):
        with self.app as client:
            # No session setup to simulate missing login
            
            form_data = {
                "review_id": str(ObjectId()),
                "feedback": "Great job!"
            }
            response = client.post('/submit_feedback', data=form_data)
            
            # Expect a redirect to the login page
            self.assertEqual(response.status_code, 302)
            self.assertIn('/login', response.location)

    @patch("application.mongo.db.form_reviews.update_one")
    def test_submit_feedback_invalid_review_id(self, mock_update_one):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'coach@example.com'
            
            # Use an invalid review_id format
            form_data = {
                "review_id": "invalid_id",
                "feedback": "Great job!"
            }
            response = client.post('/submit_feedback', data=form_data)
            
            # Expect redirect back to submit_feedback or an error flash message
            self.assertEqual(response.status_code, 302)
            self.assertIn('/submit_feedback', response.location)

    def test_set_reminder_post_missing_fields(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'coach@example.com'
            
            # Missing "date" and "time" fields
            form_data = {
                "student_id": "12345",
                "reminder": "Drink water"
            }
            response = client.post('/set_reminder', data=form_data)
            
            self.assertEqual(response.status_code, 400)

    def test_coach_dashboard_unauthorized_access(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'student@example.com'
            
            response = client.get('/coach_dashboard')
            
            self.assertEqual(response.status_code, 302)
            self.assertIn('/login', response.location)

    def test_upload_exercise_video_get_unauthorized_access(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'coach@example.com'
            
            response = client.get('/upload_exercise_video')
            self.assertEqual(response.status_code, 302)

    @patch("application.mongo.db.meetings.insert_one")
    def test_schedule_meeting_post_invalid_student_id(self, mock_insert_one):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'coach@example.com'
            
            form_data = {
                "student_id": "invalid_id",
                "date": "2024-11-01",
                "time": "08:00",
                "link": "http://meeting.link"
            }
            response = client.post('/schedule_meeting', data=form_data)
            
            self.assertEqual(response.status_code, 302)
            self.assertIn('/coach_dashboard', response.location)

    @patch("application.mongo.db.profile")  
    @patch("application.mongo.db.user")
    def test_schedule_meeting_get(self, mock_user_collection, mock_profile_collection):
        mock_user_collection.find_one.return_value = {
            "email": "coach@example.com",
            "name": "Coach Name"
        }

        mock_profile_collection.find.return_value = [
            {"_id": ObjectId(), "name": "Student 1"},
            {"_id": ObjectId(), "name": "Student 2"}
        ]

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'coach@example.com'
            
            response = client.get('/schedule_meeting')

            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Schedule Meeting", response.data)


    def test_schedule_meeting_post(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'coach@example.com'
            
            form_data = {
                "student_id": "12345",
                "date": "2024-11-01",
                "time": "08:00",
                "link": "http://meeting.link"
            }
            response = client.post('/schedule_meeting', data=form_data)
            self.assertEqual(response.status_code, 302)  # Redirect after scheduling
            self.assertEqual(response.location, 'http://localhost/coach_dashboard')


    @patch("application.mongo.db.form_reviews.update_one")
    def test_submit_feedback(self, mock_update_one):
        mock_update_one.return_value = MagicMock()

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'coach@example.com'
            
            form_data = {
                "review_id": str(ObjectId()),
                "feedback": "Great job!"
            }
            response = client.post('/submit_feedback', data=form_data)
            
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, 'http://localhost/coach_dashboard')


    @patch("application.mongo.db.user")
    @patch("application.mongo.db.profile")
    def test_set_reminder_get(self, mock_profile_collection, mock_user_collection):
        mock_user_collection.find_one.return_value = {
            "email": "coach@example.com",
            "name": "Coach Name"
        }

        mock_profile_collection.find.return_value = [
            {"_id": "student_id_1", "name": "Student One"},
            {"_id": "student_id_2", "name": "Student Two"}
        ]

        with self.app as client:

            with client.session_transaction() as sess:
                sess['email'] = 'coach@example.com'

            response = client.get('/set_reminder')

            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Set Reminder", response.data)


    def test_set_reminder_post(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'coach@example.com'
            
            form_data = {
                "student_id": "12345",
                "reminder": "Drink water",
                "date": "2024-11-01",
                "time": "08:00"
            }
            response = client.post('/set_reminder', data=form_data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, 'http://localhost/coach_dashboard')


    def test_upload_exercise_video_get(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'student@example.com'
            
            response = client.get('/upload_exercise_video')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Upload Exercise Video", response.data)


    def test_upload_exercise_video_post(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'student@example.com'
            
            form_data = {
                "exercise_type": "Push-ups",
                "video_link": "http://video.link"
            }
            response = client.post('/upload_exercise_video', data=form_data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, 'http://localhost/upload_exercise_video')


    @patch('application.mongo.db.profile')      
    @patch('application.mongo.db.form_reviews')  
    def test_upload_exercise_video_get(self, mock_form_reviews_collection, mock_profile_collection):
        mock_profile_collection.find_one.return_value = {
            "email": "student@example.com",
            "_id": ObjectId(),
            "coach": "Coach Name"
        }

        mock_form_reviews_collection.find.return_value = []

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'student@example.com'

            response = client.get('/upload_exercise_video')
            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Upload Exercise Video", response.data)

    @patch('application.mongo.db.user')
    @patch('application.mongo.db.profile')  
    @patch('application.mongo.db.tutorials')  
    def test_upload_tutorial_post(self, mock_tutorials_collection, mock_profile_collection, mock_user_collection):
        mock_user_collection.find_one.return_value = {
            "email": "coach@example.com",
            "name": "Coach Name"
        }

        mock_profile_collection.find.return_value = [
            {"_id": ObjectId(), "name": "Student 1"},
            {"_id": ObjectId(), "name": "Student 2"}
        ]

        mock_tutorials_collection.insert_one.return_value = MagicMock(inserted_id=ObjectId())

        mock_profile_collection.update_one.return_value = MagicMock()

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'coach@example.com'
            
            form_data = {
                "title": "New Tutorial",
                "description": "Tutorial description",
                "video_link": "http://tutorial.link",
                "assigned_students": [str(ObjectId())]
            }

            response = client.post('/upload_tutorial', data=form_data)

            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location, 'http://localhost/upload_tutorial')

    @patch('application.mongo.db.profile')  
    @patch('application.mongo.db.tutorials')  
    def test_view_assigned_tutorials_get(self, mock_tutorials_collection, mock_profile_collection):
        mock_profile_collection.find_one.return_value = {
            "email": "student@example.com",
            "_id": "student_id",
            "assigned_tutorials": [
                {"tutorial_id": "tutorial_1", "status": "Incomplete"}
            ],
            "progress": 0
        }

        mock_tutorials_collection.find_one.return_value = None

        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'student@example.com'
            
            response = client.get('/view_assigned_tutorials')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
