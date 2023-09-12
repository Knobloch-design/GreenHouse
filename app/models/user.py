#from app import login_manager


class User:
    def __init__(self, name, email, password, user_id=None):
        self.name = name
        self.email = email
        self.password = password
        self.user_id = user_id

    def __repr__(self):
        return f"<User {self.email}>"

    def get_user(self):
        return self.name, self.email, self.password

    def get_name(self):
        return self.name
    def get_id(self):
        return self.user_id

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password


# @login_manager.user_loader
# def load_user(user_id):
#     # Replace this with your actual user loading logic (e.g., database lookup)
#     return User("Test User", "test@test.com", "testpassword", user_id=user_id )

# Path: app/models/post.py
# Compare this snippet from app/routes.py:
# # app/routes.py
#