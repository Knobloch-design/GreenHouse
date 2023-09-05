# app/routes.py
from flask_login import login_user, login_required, logout_user

from app import app

from flask import render_template, flash, redirect, url_for, request

from app.models.user import User


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    return render_template('register.html', title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Replace with your actual authentication logic
        username = request.form['username']
        password = request.form['password']

        # Replace with actual user validation
        if username == 'demo' and password == 'password':
            user = User(id=1, username=username, password=password)
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('home'))

        flash('Login failed. Please check your credentials.', 'error')

    return render_template('login.html')

@app.route('/logout')
# @login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))
@app.route('/dashboard')
# @login_required # This decorator ensures that the user is logged in before accessing the dashboard route. Uncomment this line to enable this protection.
def dashboard():
    # Your protected dashboard route
    return render_template('dashboard.html')