# sensor_data/models.py

from django.db import models

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