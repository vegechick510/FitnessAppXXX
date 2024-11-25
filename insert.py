"""
Copyright (c) 2024 Shardul Rajesh Khare, Shruti Dhond, Pranav Manbhekar
This code is licensed under MIT license (see LICENSE for details)

@author: Burnout


This python file is used in and is part of the Burnout project.

For more information about the Burnout project, visit:
https://github.com/SEFall24-Team61/FitnessAppNew

"""

import json, os
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from bson.objectid import ObjectId, InvalidId
import bcrypt
import smtplib
from flask import json, jsonify, Flask
from flask import render_template, session, url_for, flash, redirect, request, Flask
from flask_mail import Mail, Message
from flask_pymongo import PyMongo
from tabulate import tabulate

from forms import (
    HistoryForm,
    RegistrationForm,
    LoginForm,
    CalorieForm,
    UserProfileForm,
    EnrollForm,
    ReviewForm,
    ProgressForm,
    StreakForm,
    ReminderForm,
    MoodForm,
)

from insert_db_data import insertfooddata, insertexercisedata
from insert_excercises import coaching_videos
import schedule
from threading import Thread
import time
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from flask_wtf import FlaskForm

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MAX_ALLOWED_MODULES = 100


@app.route("/proxy/font-awesome.js")
def proxy_fontawesome():
    import requests

    # Use the standard FontAwesome CDN URL
    external_url = (
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/js/all.min.js"
    )
    response = requests.get(external_url)

    # Pass the content and content type back to the client
    return (
        response.content,
        response.status_code,
        {"Content-Type": response.headers["Content-Type"]},
    )


app = Flask(__name__, template_folder="templates", static_url_path="/static")
app.secret_key = "secret"
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/test"
app.config["MONGO_CONNECT"] = False
mongo = PyMongo(app)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "burnoutapp2023@gmail.com"
app.config["MAIL_PASSWORD"] = "jgny mtda gguq shnw"
mail = Mail(app)

insertfooddata()
insertexercisedata()
coaching_videos()

# data directory
data_dir = os.path.join(os.path.dirname(__file__), "data")

# Open json file
json_file_path = os.path.join(data_dir, "exercises.json")
with open(json_file_path, "r", encoding="utf-8") as file:
    exercises = json.load(file)

# Remove folder names in image filenames
for exercise in exercises:
    images = exercise["images"]
    exercise["images"] = [image.split("/")[-1] for image in images]

# Convert the modified exercise data to a pandas DataFrame
dataframe = pd.DataFrame(exercises)

# Save the DataFrame to a CSV file
csv_file_path = os.path.join(data_dir, "exercises.csv")
dataframe.to_csv(csv_file_path, index=False, sep=",")
csv_cleaned_file_path = os.path.join(data_dir, "exercises_cleaned.csv")

# Load the cleaned data from the CSV file
df = pd.read_csv(csv_cleaned_file_path)

# Convert the 'images' field from a string to a list and strip single quotes
df["images"] = df["images"].apply(
    lambda x: [image.strip(" '") for image in x.strip("[]").split(", ")]
)

# Connect to MongoDB
collection = mongo.db.exercises

# Insert the CSV data into MongoDB
df_dict = df.to_dict(orient="records")
collection.insert_many(df_dict)

# Define the priority for user input fields
priority_fields = [
    "primaryMuscles",
    "level",
    "equipment",
    "secondaryMuscles",
    "force",
    "mechanic",
    "category",
]

# Define priority weights
priority_weights = [20, 15, 10, 5, 3, 2, 1]

# Concatenate the relevant columns to create content for recommendations
df["content"] = df[priority_fields].apply(
    lambda row: (
        " ".join([str(val) * weight for val, weight in zip(row, priority_weights)])
    ),
    axis=1,
)

# Create a TF-IDF vectorizer to convert the content into numerical form
tfidf_vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf_vectorizer.fit_transform(df["content"])

email = "mibybymi@163.com"
default_order = [
    "upcoming-meetings",
    "workout-streak",
    "gallery",
    "must-try",
    "most-popular",
    "meditation",
    "carousel-1",
    "introduction-video",
    "workout-reminder",
    "progress-bar",
    "fitness-recipes",
]
mongo.db.module_order.insert_one({"email": email, "order": default_order})
