# app/models/sensor.py

from datetime import datetime
from app import db

class SensorReading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, value):
        self.user_id = user_id
        self.value = value
