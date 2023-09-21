# greenhouse/scripts/populate_sensor_readings.py

import os
import random
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sproutsmart_project.settings")
django.setup()
from django.conf import settings
from django.db import connection

print(settings.DATABASES)
connection.connect()

from django.contrib.auth.models import User
from greenhouse.models import SensorReading

class SensorManager:
    def __init__(self):
        self.sensors = {}

    def add_sensor(self, sensor_name, sensor_type):
        if sensor_name not in self.sensors:
            self.sensors[sensor_name] = sensor_type()
        else:
            raise ValueError(f"Sensor with name '{sensor_name}' already exists.")

    def get_sensor(self, sensor_name):
        if sensor_name in self.sensors:
            return self.sensors[sensor_name]
        else:
            raise ValueError(f"Sensor with name '{sensor_name}' does not exist.")

    def get_sensor_names(self):
        return list(self.sensors.keys())


    def simulate_sensor_readings(self, user_id, num_readings=10):
        for _ in range(num_readings):
            temperature_sensor = self.get_sensor("temperature")
            humidity_sensor = self.get_sensor("humidity")
            soil_moisture_sensor = self.get_sensor("soil_moisture")

            SensorReading.objects.create(
                user_id=user_id,
                type= "temperature",
                value=temperature_sensor.read() if temperature_sensor else None,
            )

            SensorReading.objects.create(
                user_id=user_id,
                type= "humidity",
                value=humidity_sensor.read() if humidity_sensor else None,
            )

            SensorReading.objects.create(
                user_id=user_id,
                type= "soil_moisture",
                value=soil_moisture_sensor.read() if soil_moisture_sensor else None,
            )



class TemperatureSensor:
    def __init__(self):
        self.value = None

    def read(self):
        # Simulate temperature reading within a reasonable range (e.g., 0°C to 40°C)
        self.value = round(random.uniform(0, 40), 2)
        return self.value

class HumiditySensor:
    def __init__(self):
        self.value = None

    def read(self):
        # Simulate humidity reading within a reasonable range (e.g., 20% to 80%)
        self.value = round(random.uniform(20, 80), 2)
        return self.value
class SoilMoistureSensor:
    def __init__(self):
        self.value = None

    def read(self):
        # Simulate soil moisture reading within a reasonable range (e.g., 10% to 70%)
        self.value = round(random.uniform(10, 70), 2)
        return self.value

if __name__ == "__main__":

    user_id = 1  # Replace with the user ID of the desired user.
    user, created = User.objects.get_or_create(id=user_id)

    sensor_manager = SensorManager()
    sensor_manager.add_sensor("temperature", TemperatureSensor)
    sensor_manager.add_sensor("humidity", HumiditySensor)
    sensor_manager.add_sensor("soil_moisture", SoilMoistureSensor)

    sensor_manager.simulate_sensor_readings(user_id)
