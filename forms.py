
"""
Copyright (c) 2024 Shardul Rajesh Khare, Shruti Dhond, Pranav Manbhekar
This code is licensed under MIT license (see LICENSE for details)

@author: Burnout


This python file is used in and is part of the Burnout project.

For more information about the Burnout project, visit:
https://github.com/SEFall24-Team61/FitnessAppNew

"""

# from datetime import date
# from re import sub
# from flask import app
"""Importing modules to create forms"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, DateField,FloatField, TextAreaField, SubmitField, IntegerField
from wtforms.fields.core import DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional, NumberRange
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
            print("Base validation failed.")
            return False

        # Debugging user type
        print("User type data:", self.user_type.data)

        if self.user_type.data == 'student':
            print("Validating student-specific fields")
            # Check if all student-specific fields are filled
            required_fields = [self.weight, self.height, self.goal, self.target_weight, self.coach]
            missing_fields = [field.label.text for field in required_fields if not field.data]
            
            if missing_fields:
                for field in required_fields:
                    if not field.data:
                        field.errors.append(f"{field.label.text} is required for students.")
                print("Missing fields for student:", missing_fields)
                return False

        elif self.user_type.data == 'coach':
            print("Validating coach-specific fields")
            # Check if all coach-specific fields are filled
            if not self.specialization.data:
                self.specialization.errors.append('Specialization is required for coaches.')
            if self.experience.data is None or self.experience.data < 0:
                self.experience.errors.append('Experience is required for coaches and must be a non-negative number.')
            
            if self.specialization.errors or self.experience.errors:
                print("Coach field errors:", self.specialization.errors, self.experience.errors)
                return False

        return True


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

class ProgressForm(FlaskForm):
    # Weight
    date = DateField('Date', format='%Y-%m-%d', validators=[Optional()])
    current_weight = DecimalField('Current Weight (kg)', validators=[Optional(), NumberRange(min=0, max=500, message="Current Weight must be between 0 and 500 kg")])

    goal_weight = DecimalField('Goal Weight (kg)', validators=[Optional(), NumberRange(min=0, max=500, message="Goal Weight must be between 0 and 500 kg")])
    
    # Measurements
    waist = DecimalField('Waist (cm)', validators=[Optional(), NumberRange(min=50, max=150, message="Waist must be between 50 and 150 cm")])
    hips = DecimalField('Hips (cm)', validators=[Optional(), NumberRange(min=70, max=160, message="Hips must be between 70 and 160 cm")])
    chest = DecimalField('Chest (cm)', validators=[Optional(), NumberRange(min=70, max=500, message="Chest must be between 70 and 150 cm")])
    
    # Additional Notes
    notes = TextAreaField('Notes', validators=[Optional()])
    
    submit = SubmitField('Submit')


class ReminderForm(FlaskForm):
    # Weight
    reminder_email = StringField('Reminder Email', validators=[Optional(), Email()])
    set_date = DateField('Set Date', format='%Y-%m-%d', validators=[Optional()])

    reminder_type = SelectField('Reminder Type', choices=[('goal', 'Goal'), ('workout', 'Workout')], validators=[DataRequired()])

    # Goal-specific fields
    goal_weight = DecimalField('Goal Weight (kg)', validators=[Optional(), NumberRange(min=0, max=500, message="Goal Weight must be between 0 and 500 kg")])

    # Workout-specific fields
    workout_title = SelectField('Workout Plan', choices=[], validators=[Optional()])

    # Additional Notes
    notes = TextAreaField('Notes', validators=[Optional()])
    
    submit = SubmitField('Submit')


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

class StreakForm(FlaskForm):
    """Form to manage workout streak updates"""
    
    current_streak = IntegerField('Current Streak (days)', validators=[Optional()], render_kw={'readonly': True})
    new_streak = IntegerField('Start New Streak (days)', validators=[Optional()])
    update_streak = IntegerField('Update Streak (days)', validators=[Optional()])
    notes = StringField('Notes (Optional)', validators=[Optional()])
    
    submit = SubmitField('Save Streak')