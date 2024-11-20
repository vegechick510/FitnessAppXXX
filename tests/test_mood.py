"""
Copyright (c) 2024 
This code is licensed under MIT license (see LICENSE for details)

@author: Burnout


This python file is used in and is part of the Burnout project.

For more information about the Burnout project, visit:

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

    def test_mood_tracker_route_access_1(self):
        """
        test login
        """
        response = self.app.get('/mood_tracker', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b"Log In", response.data)  


    def test_mood_tracker_route_access_2(self):
        """
        test login
        """
        response = self.app.get('/mood_tracker', follow_redirects=True)
        #self.assertEqual(response.status_code, 200)
        self.assertIn(b"Log In", response.data)
      

    def test_mood_tracker_form_render_1(self):
        """
        test 
        """
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'  # 模拟登录用户

            response = client.get('/mood_tracker')
            self.assertEqual(response.status_code, 200)
            #self.assertIn(b"Track Your Mood", response.data)  # 页面标题
            #self.assertIn(b"Mood Description", response.data)  # 表单字段
            #self.assertIn(b"Submit", response.data)  # 提交按钮

    def test_mood_tracker_form_render_2(self):
        """
        测试登录用户是否能够正确访问并渲染表单
        """
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'  # 模拟登录用户

            response = client.get('/mood_tracker')
            #self.assertEqual(response.status_code, 200)
            self.assertIn(b"Track Your Mood", response.data)  # 页面标题
            #self.assertIn(b"Mood Description", response.data)  # 表单字段
            #self.assertIn(b"Submit", response.data)  # 提交按钮

    def test_mood_tracker_form_render_3(self):
        """
        test if the login user can render
        """
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'  # 模拟登录用户

            response = client.get('/mood_tracker')
            #self.assertEqual(response.status_code, 200)
            #self.assertIn(b"Track Your Mood", response.data)  # 页面标题
            self.assertIn(b"Mood Description", response.data)  # 表单字段
            #self.assertIn(b"Submit", response.data)  # 提交按钮

    def test_mood_tracker_form_render_4(self):
        """
        测试登录用户是否能够正确访问并渲染表单
        """
        with self.app as client:
            with client.session_transaction() as sess:
                sess['email'] = 'testuser@example.com'  # 模拟登录用户

            response = client.get('/mood_tracker')
            #self.assertEqual(response.status_code, 200)
            #self.assertIn(b"Track Your Mood", response.data)  # 页面标题
            #self.assertIn(b"Mood Description", response.data)  # 表单字段
            self.assertIn(b"Submit", response.data)  # 提交按钮

if __name__ == '__main__':
    unittest.main()