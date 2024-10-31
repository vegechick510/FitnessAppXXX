
"""
Copyright (c) 2023 Rajat Chandak, Shubham Saboo, Vibhav Deo, Chinmay Nayak
This code is licensed under MIT license (see LICENSE for details)

@author: Burnout


This python file is used in and is part of the Burnout project.

For more information about the Burnout project, visit:
https://github.com/VibhavDeo/FitnessApp

"""
# from datetime import date
# from re import sub
# from flask import app
"""Importing modules to create forms"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField, FloatField, BooleanField, SelectMultipleField # Import FloatField
from wtforms.fields.core import DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, Optional
from apps import App


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    user_type = SelectField('User Type', choices=[('', 'Please select user type'), ('student', 'Student'), ('coach', 'Coach')], validators=[DataRequired()])

    
    # Student-specific fields
    weight = FloatField('Weight', validators=[Optional(), NumberRange(min=20, max=200)])
    height = FloatField('Height', validators=[Optional(), NumberRange(min=100, max=250)])
    goal = StringField('Goal', validators=[Optional(), Length(min=2, max=50)])
    target_weight = FloatField('Target Weight', validators=[Optional(), NumberRange(min=20, max=200)])
    coach = SelectField('Coach', choices=[], validators=[Optional()])  # Dropdown for student to select a coach
    
    # Coach-specific fields
    specialization = SelectField(
        'Specialization', 
        choices=[
            ('yoga', 'Yoga'), 
            ('strength', 'Strength Training'), 
            ('cardio', 'Cardio'), 
            ('nutrition', 'Nutrition Coaching'),
            ('pilates', 'Pilates'),
            ('crossfit', 'CrossFit')
        ], 
        validators=[Optional()],
    )
    experience = FloatField('Experience (years)', validators=[Optional(), NumberRange(min=0)])  

    submit = SubmitField('Sign Up')

    def validate(self):
        """Override validate to conditionally apply field validation based on user_type."""
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        if self.user_type.data == 'student':
            if not self.weight.data or not self.height.data or not self.goal.data or not self.target_weight.data or not self.coach.data:
                if not self.weight.data:
                    self.weight.errors.append('Weight is required for students.')
                if not self.height.data:
                    self.height.errors.append('Height is required for students.')
                if not self.goal.data:
                    self.goal.errors.append('Goal is required for students.')
                if not self.target_weight.data:
                    self.target_weight.errors.append('Target Weight is required for students.')
                if not self.coach.data:
                    self.coach.errors.append('Coach selection is required for students.')
                return False

        if self.user_type.data == 'coach':
            if not self.specialization.data:
                self.specialization.errors.append('Specialization is required for coaches.')
            if self.experience.data is None or self.experience.data < 0:
                self.experience.errors.append('Experience is required for coaches and must be a non-negative number.')
            return bool(self.specialization.data and self.experience.data is not None and self.experience.data >= 0)



class LoginForm(FlaskForm):
    """Login form to log in to the application"""
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class CalorieForm(FlaskForm):
    """Form to rcord the calorie intake details of the user"""
    app = App()
    mongo = app.mongo

    cursor = mongo.db.food.find()
    get_docs = []
    for record in cursor:
        get_docs.append(record)

    result = []
    temp = ""
    for i in get_docs:
        temp = i['food'] + ' (' + i['calories'] + ')'
        result.append((temp, temp))

    food = SelectField(
        'Select Food', choices=result)

    burnout = StringField('Burn Out', validators=[DataRequired()])
    submit = SubmitField('Save')


class UserProfileForm(FlaskForm):
    """Form to input user details to store their height, weight, goal and target weight"""
    weight = StringField(
        'Weight', validators=[
            DataRequired(), Length(
                min=2, max=20)])
    height = StringField(
        'Height', validators=[
            DataRequired(), Length(
                min=2, max=20)])
    goal = StringField(
        'Goal (Weight Loss/ Muscle Gain)', validators=[
            DataRequired(), Length(
                min=2, max=20)])
    target_weight = StringField(
        'Target Weight', validators=[
            DataRequired(), Length(
                min=2, max=20)])
    submit = SubmitField('Update')


class HistoryForm(FlaskForm):
    """Form to input the date for which the history needs to be displayed"""
    app = App()
    mongo = app.mongo
    date = DateField()
    submit = SubmitField('Fetch')


class EnrollForm(FlaskForm):
    """Form to enroll into a particular exercise/event"""
    app = App()
    mongo = app.mongo
    submit = SubmitField('Enroll')

class ResetPasswordForm(FlaskForm):
    """Form to reset the account password"""
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm Password', validators=[
            DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset')

class ReviewForm(FlaskForm):
    """Form to input the different reviews about the application"""
    review = StringField(
        'Review', validators=[
            DataRequired(), Length(
                min=2, max=200)])
    name = StringField(
        'Name', validators=[
            DataRequired(), Length(
                min=2, max=200)])
    submit = SubmitField('Submit')
