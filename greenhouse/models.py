from django.db import models

# greenhouse/models.py

from django.db import models
from django.contrib.auth.models import User
import uuid

class User(User):
    uuid =  models.UUIDField(default=uuid.uuid4, editable=False)
    # Add other fields as needed


class SensorReading(models.Model):
    valid_sensors = [("temp","temperature"), ("humidity","humidity"), ("moisture","soil_moisture")]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=valid_sensors, max_length=100, default="temp")
    value = models.FloatField()

    def __str__(self):
        return f"Sensor Reading (User: {self.user.username}, Value: {self.value})"
