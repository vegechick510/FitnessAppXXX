"""from datetime import datetime, timedelta
from types import MethodDescriptorType
"""
from bson.objectid import ObjectId

from flask_wtf import form
#from utilities import Utilities
from flask import app, render_template, session, url_for, flash, redirect, request, Response, Flask
from flask_pymongo import PyMongo
#from flask import json
from flask.helpers import make_response
#from flask.json import jsonify
from flask_mail import Mail, Message
from forms import RegistrationForm, LoginForm
import bcrypt
#from apps import App
from flask_login import LoginManager, login_required
from bson.objectid import ObjectId


app = Flask(__name__)
app.secret_key = 'secret'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'
mongo = PyMongo(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "bogusdummy123@gmail.com"
app.config['MAIL_PASSWORD'] = "helloworld123!"
mail = Mail(app)

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
# ############################ 
# login() function displays the Login form (login.html) template
# route "/login" will redirect to login() function.
# LoginForm() called and if the form is submitted then various values are fetched and verified from the database entries
# Input: Email, Password, Login Type 
# Output: Account Authentication and redirecting to Dashboard
# ########################## 
    if not session.get('email'):
        form = LoginForm()
        if form.validate_on_submit():
            temp = mongo.db.user.find_one({'email': form.email.data}, {
                                         'email', 'pwd', 'temp'})
            if temp is not None and temp['email'] == form.email.data and (
                bcrypt.checkpw(
                    form.password.data.encode("utf-8"),
                    temp['pwd']) or temp['temp'] == form.password.data):
                flash('You have been logged in!', 'success')
                session['email'] = temp['email']
                return redirect(url_for('dashboard'))
            else:
                flash(
                    'Login Unsuccessful. Please check username and password',
                    'danger')
    else:
        return redirect(url_for('home'))
    return render_template(
        'login.html',
        title='Login',
        form=form,
        type=form.type.data)



@app.route("/logout", methods=['GET', 'POST'])
def logout():
# ############################ 
# logout() function just clears out the session and returns success
# route "/logout" will redirect to logout() function.
# Output: session clear 
# ########################## 
    session.clear()
    return "success"


@app.route("/register", methods=['GET', 'POST'])
def register():
# ############################ 
# register() function displays the Registration portal (register.html) template
# route "/register" will redirect to register() function.
# RegistrationForm() called and if the form is submitted then various values are fetched and updated into database
# Input: Username, Email, Password, Confirm Password
# Output: Value update in database and redirected to home login page
# ########################## 
    if not session.get('email'):
        form = RegistrationForm()
        if form.validate_on_submit():
            if request.method == 'POST':
                username = request.form.get('username')
                email = request.form.get('email')
                password = request.form.get('password')
                id = mongo.db.user.insert({'name': username, 'email': email, 'pwd': bcrypt.hashpw(
                    password.encode("utf-8"), bcrypt.gensalt()), 'temp': None})
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

@app.route("/common", methods=['GET', 'POST'])
def common():
    return render_template('common.html', title='Common')



if __name__ == '__main__':
    app.run(debug=True)