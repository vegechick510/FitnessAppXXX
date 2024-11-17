reminder_email()
- This function sends an automated email to all the users as a daily reminder to exercise

login()
- This function is used for login by the user
- Using email ID and passoword is validated and the user is directed to home

logout()
- This function is used for logout by the user
- logout() function just clears the session

register()
- This function is used for registering new users
- Details of new users are stored in the database and the user is redirected to login page

homePage()
- This function renders the home page

send_email()
- This function is used to send an email to user's friends containing calorie history of user
- The user will fill a textarea with their friends email IDs (comma seperated if multiple)

calories()
- This function will add calories consumedburned for the data selected.

profile()
- This function is used to storedisplay user's profile details such as height, weight and goal weight

history()
- This function displays user's historical calorie consumption and burnout at date level

friends()
- This function allows user to accept friend requests and display all friends

bmi_calci()
- This function returns the Body Mass Index of the user whenever they enter their height and weight

submit_reviews()
- This function returns the exiting reviews and also insert the new reviews submitted by user

calc_bmi()
- This function calculates the BMI mathematically which is returned to the the bmi_calci() function

get_bmi_category()
- This function will designate the BMI category of the user based on the calculated BMI value

send_email()
- This function shares the calorie details of the user to their friends via email.

add_favorite()
- This function allows the user to record and store their favourite exercises

favorites()
- This function displays the favourite exercises of the users

yoga()/swim()/abbs()/belly()/core()/gym()/walk()/dance()/hrx()
- This function allows user to enroll in different plans

recommend_workout() 
- This function renders the workout recommendation page for users to select their fitness level

beginner() 
- This function displays beginner-level workouts based on the primary muscle group

advanced() 
- This function displays advanced-level workouts based on the primary muscle group

recommend() 
- This function generates workout recommendations based on user inputs

more_recommendations() 
- This function provides additional workout recommendations based on item-based collaborative filtering

progress_monitor()
- This function allows users to log their daily progress, weight, measurements, etc.

progress_history() 
- This function shows the user's progress history with data visualizations

reminders() 
- This function shows the user's reminder settings

wellness_log() 
- This function displays the wellness log page

update_streak() 
- This function updates the user's workout streak based on activity

workout_streak() 
- This function shows the user's current workout streak

display_profile()
- This function displays the user profile with weight progress graph

user_profile() 
- This function allows users to update profile details such as height, weight, and goals

water() 
- This function logs and displays daily water intake along with averages

clear-intake() 
- This function clears the user's water intake records

shop() 
- This function renders the shop page for available items

ajaxhistory() 
- This function fetches calorie history for a specific date via AJAX

community() 
- This function renders a page for managing friends, including adding, approving, and listing friends

delete_friend() 
- This function deletes a specified friend from the user’s friend list

ajaxsendrequest() 
- This function sends a friend request to another user

ajaxcancelrequest() 
- This function cancels a sent friend request

ajaxapproverequest() 
- This function approves a received friend request

dashboard() 
- This function displays the dashboard with user-specific activities and meeting information

add_favorite() 
- This function adds or removes an exercise from the user's favorites list

favorites() 
- This function shows the user's list of favorite exercises

submit_review() 
- This function allows students to submit reviews for their assigned coach

blog() 
- This function displays a blog page

coach_dashboard() 
- This function displays the coach's dashboard with student progress and review information

schedule_meeting() 
- This function allows coaches to schedule meetings with assigned students

submit_feedback() 
- This function allows coaches to submit feedback on a student's form review

set_reminder() 
- This function allows coaches to set reminders for students

coach_reviews() 
- This function displays reviews for the coach along with student progress data

upload_exercise_video() 
- This function allows students to upload exercise videos for their coach's review

coach_profile()
 - This function displays the coach's profile with reviews and assigned students

upload_tutorial() 
- This function allows coaches to upload tutorial videos for students

view_assigned_tutorials() 
- This function displays tutorials assigned to the student and allows marking them as completed

manage_plans() 
- This function enables coaches to create, edit, and assign workout plans to students

student_plans() 
- This function allows students to view their assigned workout plans
