import threading

import paho.mqtt.client as mqtt

# Global variable to store formatted data

formatted_data = ""
data_lock = threading.Lock()
last_data = ""


class MQTTClient:
    def __init__(self):
        self.client = self.setup_client()
        self.last_data = last_data

    def on_message(self, client, userdata, message):
        global formatted_data  # Declare global variable
        payload = message.payload.decode("utf-8")
        print(f"Received message '{payload}' on topic '{message.topic}'")

        # Format and store the data in the global variable
        formatted_data = format_message(payload)
        self.last_data = formatted_data

    def setup_client(self):
        client = mqtt.Client()
        client.on_message = self.on_message
        client.connect("localhost", 1883)
        client.subscribe("sensors/data")
        return client

    def get_last_data(self):
        return self.last_data

    def __repr__(self):
        return f"MQTTClient(last_data={self.last_data})"

mqtt_client = MQTTClient()



def parse_message(input_str):
    try:
        # Parse the input string into a tuple of floats
        data = eval(input_str)

        # Check if the tuple has the expected length (4)
        if len(data) != 4:
            raise ValueError("Input tuple should have 4 values")

        # Extract individual values
        temperature, humidity, moisture, probe_temperature = data
    except (ValueError, SyntaxError) as e:
        return str(e)
    return [temperature, humidity, moisture, probe_temperature]

def format_message(input_str):
    try:
        # Parse the input string into a tuple of floats
        data = eval(input_str)

        # Check if the tuple has the expected length (4)
        if len(data) != 4:
            raise ValueError("Input tuple should have 4 values")

        # Extract individual values
        temperature, humidity, moisture, probe_temperature = data

        # Format the values with 2 decimal places
        formatted_temperature = f"Temperature: {temperature:.2f}°C"
        formatted_humidity = f"Humidity: {humidity:.2f}%"
        formatted_moisture = f"Moisture: {moisture:.2f}%"
        formatted_probe_temperature = f"Probe_Temperature: {probe_temperature:.2f}°C"

        # Concatenate the formatted values
        formatted_result = ", ".join(
            [formatted_temperature, formatted_humidity, formatted_moisture, formatted_probe_temperature])

        return formatted_result
    except (ValueError, SyntaxError) as e:
        return str(e)

def on_message(client, userdata, message):
    global formatted_data  # Declare global variable
    payload = message.payload.decode("utf-8")
    print(f"Received message '{payload}' on topic '{message.topic}'")

    # Format and store the data in the global variable
    formatted_data = format_message(payload)

def do_main():

    client = mqtt.Client()
    client.on_message = on_message
    client.connect("localhost", 1883)
    client.subscribe("sensors/data")
    while True:
        client.loop()

if __name__ == "__main__":
    while True:
        do_main()
