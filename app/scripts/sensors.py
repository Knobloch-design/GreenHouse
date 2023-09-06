# sensor_manager.py
import random
class SensorManager:
    def __init__(self):
        self.sensors = {}

    def add_sensor(self, sensor_name, sensor_type):
        # Add a new sensor to the manager
        if sensor_name not in self.sensors:
            self.sensors[sensor_name] = sensor_type()
        else:
            raise ValueError(f"Sensor with name '{sensor_name}' already exists.")

    def get_sensor(self, sensor_name):
        # Get a sensor instance by name
        if sensor_name in self.sensors:
            return self.sensors[sensor_name]
        else:
            raise ValueError(f"Sensor with name '{sensor_name}' does not exist.")

    def get_all_sensors(self):
        # Get a list of all sensor names
        return list(self.sensors.keys())

# Example sensor classes
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
class HumiditySensor:
    def __init__(self):
        self.value = None

    def read(self):
        # Code to read humidity from the sensor
        # Replace this with actual sensor reading logic
        self.value = round(random.uniform(60, 90), 2)
        return self.value

class SoilMoistureSensor:
    def __init__(self):
        self.value = None

    def read(self):
        # Simulate soil moisture reading within a reasonable range (e.g., 10% to 70%)
        self.value = round(random.uniform(10, 70), 2)
        return self.value

if __name__ == "__main__":
    # Example usage of the Sensor Manager
    sensor_manager = SensorManager()
    sensor_manager.add_sensor("temperature", TemperatureSensor)
    sensor_manager.add_sensor("humidity", HumiditySensor)
    sensor_manager.add_sensor("soil_moisture", SoilMoistureSensor)

    temperature_sensor = sensor_manager.get_sensor("temperature")
    humidity_sensor = sensor_manager.get_sensor("humidity")
    soil_moisture_sensor = sensor_manager.get_sensor("soil_moisture")

    print(f"Temperature: {temperature_sensor.read()}°C")
    print(f"Humidity: {humidity_sensor.read()}%")
    print(f"Soil Moisture: {soil_moisture_sensor.read()}%")
