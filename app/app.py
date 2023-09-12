# app/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


# app/routes.py
from flask_login import login_user, login_required, logout_user


from flask import render_template, flash, redirect, url_for, request

from models.user import User

# def create_app():
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sprout_smart.sqlite'
#
#     db.init_app(app)
#     login_manager = LoginManager()
#     login_manager.login_view = 'auth.login'
#     login_manager.init_app(app)
#     # app.config.from_object()
#     # register_extensions(app)
#
#     return app
#
#     # # app.config.from_object()
#     # register_extensions(app)
#
# # def register_extensions(app):
# #     db.init_app(app)
#
#
#
# # app/routes.py
#
#
# if __name__ == "__main__":
#     app = create_app()
#     app.run(debug=True)

app = Flask(__name__)
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
if __name__ == "__main__":
    app.run(debug=True)