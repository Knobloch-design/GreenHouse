# sensor_data/models.py

from django.db import models

import backend.settings


class SensorReading(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Greenhouse(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='greenhouses', on_delete=models.CASCADE)
    # Use related_name to specify the name of the reverse relationship
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey.related_name
    # https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_one/
    # https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/
    # https://docs.djangoproject.com/en/3.2/topics/db/examples/one_to_one/


class ControlSignals(models.Model):
    heating_pad = models.BooleanField(default=False)
    light = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    greenhouse = models.ForeignKey(Greenhouse, related_name='control_signals', on_delete=models.CASCADE)

    def __str__(self):
        return f"Heating Pad: {self.heating_pad}, Light: {self.light}"


if __name__ == "__main__":
    from .models import Greenhouse, ControlSignals
    from django.contrib.auth.models import User  # Import the User model
    from backend import settings  # Import the DATABASES dictionary
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_SETTINGS_MODULE)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", INSTALLED_APPS)  # Set the DJANGO_SETTINGS_MODULE environment variable
    # Create a user if not already created
    user, created = User.objects.get_or_create(username="ivanjohnson-test")
    settings.configure()  # Configure the database settings
    # Create a greenhouse instance with initial values
    greenhouse = Greenhouse(
        name="Your Greenhouse Name",
        description="Your Greenhouse Description",
        location="Your Location",
        user=user,  # Assign the user you created
    )
    greenhouse.save()  # Save the greenhouse instance

    # Create a control signal instance associated with the greenhouse
    control_signals = ControlSignals(
        heating_pad=False,
        light=False,
        greenhouse=greenhouse,  # Associate with the created greenhouse
    )
    control_signals.save()  # Save the control signals instance
