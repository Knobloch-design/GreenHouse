# db_init.py
from app.models.user import User
from app import db

def init_db():
    db.create_all()
    db.session.commit()
    user = User(name="admin", email="admin@admin.com", password="admin")
    db.session.add(user)
    db.session.commit()