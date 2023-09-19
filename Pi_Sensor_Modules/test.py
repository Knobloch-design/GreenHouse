import RPi.GPIO as GPIO
import time
import drivers
import sqlite3
import pickle
from flask import Flask, jsonify, request
import json
import socket

display = drivers.Lcd()
display.lcd_backlight(0)

global current_temp
global buttonPressed
buttonPressed=False

conn = sqlite3.connect('temperature.db')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

bounceTime = 200

def connect_to_server(current_ip, port):
    global send_data_to_server
    global sock
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((current_ip, port))
        send_data_to_server = True
        print("Successfully connected to server!")
        sock.send(getTemp_all())
    except ConnectionRefusedError:
        print("Connection to server refused.")
        send_data_to_server = False
    except TimeoutError:
        print("Connection to server timed out.")
        send_data_to_server = False
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        send_data_to_server = False

def displayTemp(ev=None):
    display.lcd_on()
    display.lcd_backlight(1)
    display.lcd_display_string('Temp:{} C'.format(current_temp),1)

def displayOFF(ev = None):
    display.lcd_backlight(0)

def getTemp():
    query = 'SELECT temp_c FROM temperature ORDER BY Id DESC LIMIT 1;'
    c = conn.cursor()
    c.execute(query)
    data = c.fetchone()
    return(data[0])

def getTemp_all():
    query = 'SELECT temp_c FROM temperature ORDER BY Id DESC LIMIT 300;'
    c = conn.cursor()
    c.execute(query)
    data = c.fetchall()
    return(pickle.dumps(data))

app = Flask(__name__)

@app.route('/temperature_300')
def temperature_300():
    db = sqlite3.connect('temperature.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM temperature ORDER BY id DESC LIMIT 300')
    result = cursor.fetchall()
    db.close()
    return json.dumps(result)

@app.route('/temperature')
def temperature():
    db = sqlite3.connect('temperature.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM temperature ORDER BY id DESC LIMIT 1')
    result = cursor.fetchall()
    db.close()
    return jsonify(result)

@app.route('/', methods=['POST'])
def receive_data():
    data = request.get_json()
    value = data['value']
    # do something with the boolean value here
    return "Data received successfully."
while True:
    current_temp = getTemp()
    time.sleep(.1)
    if(GPIO.input(26) == GPIO.LOW):
        while(GPIO.input(26) == GPIO.LOW):
             current_temp = getTemp()
             displayTemp()
             print("ON")
             display.lcd_clear()
             display.lcd_backlight(0)
             print("OFF")


if __name__ == '__main__':
    app.run(host='172.23.8.137', port =5000)

