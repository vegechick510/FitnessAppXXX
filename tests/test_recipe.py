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

class TestApplication_2(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_fitness_recipes_render_1(self):

        response = self.app.get('/dashboard')
        assert response.status_code == 200

    def test_fitness_recipes_render_2(self):

        response = self.app.get('/dashboard')
        assert b"Fitness Recipes" in response.data

    def test_fitness_recipes_render_3(self):

        response = self.app.get('/dashboard')

        assert b'carousel-inner' in response.data


    def test_fitness_recipes_images_1(self):
        response = self.app.get('/dashboard')

        assert b"recipe1.png" in response.data

    def test_fitness_recipes_images_2(self):
        response = self.app.get('/dashboard')
        assert b"recipe2.png" in response.data

    def test_fitness_recipes_images_3(self):
        response = self.app.get('/dashboard')
        assert b"recipe3.png" in response.data

    def test_fitness_recipes_images_4(self):
        response = self.app.get('/dashboard')
        assert b"Grilled Chicken Salad" in response.data

    def test_fitness_recipes_images_5(self):
        response = self.app.get('/dashboard')
        assert b"Protein Smoothie Bowl" in response.data

    def test_fitness_recipes_images_6(self):
        response = self.app.get('/dashboard')
        assert b"Quinoa Veggie Stir-fry" in response.data

    def test_fitness_recipes_content_1(self):

        response = self.app.get('/dashboard')
        assert response.status_code == 200

    def test_fitness_recipes_content_2(self):

        response = self.app.get('/dashboard')
        assert b"Grilled Chicken Salad" in response.data

    def test_fitness_recipes_content_3(self):

        response = self.app.get('/dashboard')

        assert b"Protein Smoothie Bowl" in response.data

    def test_fitness_recipes_content_4(self):

        response = self.app.get('/dashboard')

        assert b"Quinoa Veggie Stir-fry" in response.data

    def test_fitness_recipes_content_5(self):

        response = self.app.get('/dashboard')

        assert b"A high-protein, low-carb salad with greens, grilled chicken" in response.data

    def test_fitness_recipes_content_6(self):

        response = self.app.get('/dashboard')

        assert b"A delicious smoothie bowl with protein powder, fresh fruits" in response.data

    def test_fitness_recipes_content_7(self):

        response = self.app.get('/dashboard')

        assert b"A healthy stir-fry with quinoa, broccoli, bell peppers" in response.data


    def test_fitness_recipes_carousel_controls_1(self):
        response = self.app.get('/dashboard')
        assert b'carousel-control-prev' in response.data


    def test_fitness_recipes_carousel_controls_2(self):
        response = self.app.get('/dashboard')
        assert b'carousel-control-prev-icon' in response.data

    def test_fitness_recipes_carousel_controls_3(self):
        response = self.app.get('/dashboard')
        assert b'carousel-control-next' in response.data

    def test_fitness_recipes_carousel_controls_4(self):
        response = self.app.get('/dashboard')
        assert b'carousel-control-next-icon' in response.data


    def test_fitness_recipes_carousel_controls_5(self):
        response = self.app.get('/dashboard')
        assert b'carousel-control-prev' in response.data
        assert b'carousel-control-next' in response.data
        assert b'carousel-control-next-icon' in response.data


    def test_fitness_recipes_carousel_controls_6(self):
        response = self.app.get('/dashboard')
        assert b'carousel-control-next-icon' in response.data
        assert b'carousel-control-prev-icon' in response.data