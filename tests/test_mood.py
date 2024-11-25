"""
Copyright (c) 2024 
This code is licensed under MIT license (see LICENSE for details)

@author: Burnout


This python file is used in and is part of the Burnout project.

For more information about the Burnout project, visit:

"""

import unittest
import os, sys, inspect
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

    def test_mood_tracker_route_access_1(self):
        response = self.app.get("/mood_tracker", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_mood_tracker_route_access_2(self):
        response = self.app.get("/mood_tracker", follow_redirects=True)
        self.assertIn(b"Log In", response.data)

    def test_mood_tracker_route_access_3(self):
        response = self.app.get("/mood_tracker", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # self.assertIn(b"Log In.", response.data)

    def test_mood_tracker_form_render_1(self):
        """
        test
        """
        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"

            response = client.get("/mood_tracker")
            self.assertEqual(response.status_code, 200)

    def test_mood_tracker_form_render_2(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"

            response = client.get("/mood_tracker")
            self.assertIn(b"Track Your Mood", response.data)

    def test_mood_tracker_form_render_3(self):
        """
        test if the login user can render
        """
        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"
            response = client.get("/mood_tracker")
            self.assertIn(b"Mood Description", response.data)

    def test_mood_tracker_form_render_4(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"
            response = client.get("/mood_tracker")

            self.assertIn(b"Submit", response.data)

    def test_mood_tracker_form_render_5(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"
            response = client.get("/mood_tracker")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Submit", response.data)

    def test_mood_tracker_form_render_6(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"
            response = client.get("/mood_tracker")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Mood Description", response.data)

    def test_mood_tracker_form_render_7(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"
            response = client.get("/mood_tracker")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Track Your Mood", response.data)

    def test_mood_tracker_form_render_8(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"
            response = client.get("/mood_tracker")
            self.assertIn(b"Track Your Mood", response.data)
            self.assertIn(b"Mood Description", response.data)

    def test_mood_tracker_form_render_9(self):

        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"
            response = client.get("/mood_tracker")
            self.assertIn(b"Mood Description", response.data)
            self.assertIn(b"Submit", response.data)

    def test_mood_tracker_form_submission(self):
        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "testuser@example.com"

            form_data = {
                "type": "before",
                "mood": "Feeling great before workout!",
                "submit": True,
            }
            response = client.post(
                "/mood_tracker", data=form_data, follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            # self.assertIn(b"Mood successfully saved", response.data)


if __name__ == "__main__":
    unittest.main()
