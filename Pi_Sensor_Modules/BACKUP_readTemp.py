import os
import glob
import sqlite3
import socket
import time
import drivers  # assuming this is a custom module
import os
from twilio.rest import Client  # importing Twilio library
import socket
MAX_TEMP =50  # maximum temperature threshold
MIN_TEMP = 11  # minimum temperature threshold
# Define the server's IP address and port
current_ip = '172.17.30.81'
port = 4000
import socket


# Set environment variables for your Twilio account credentials
# These credentials are used to authenticate and authorize requests
# Read more at http://twil.io/secure
account_sid = "ACbf396ebc5e1bbc372058a638333639a0"
auth_token = "d033deee8f868450922759c6b0bc5a7c"
client = Client(account_sid, auth_token)  # creating Twilio client object


# Load the necessary kernel modules to read the temperature from thermocouple
os.system('modprobe w1-gpio')  # load kernel module for GPIO interface of 1-wire bus
os.system('modprobe w1-therm')  # load kernel module for temperature measurement via 1-wire bus
device_file = '/sys/bus/w1/devices/28-3c80e3819f89/w1_slave'  # path to the device file that stores temperature data


# Create a connection object to the SQLite database 'temperature.db'
conn = sqlite3.connect('temperature.db')
# Create a cursor object to execute SQL queries
cursor = conn.cursor()

def connect_to_server(current_ip, port):
    global send_data_to_server
    global sock
    try:
        # Replace host and port with the server's address and port number
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((current_ip, port))
        send_data_to_server = True
        print("Successfully connected to server!")
    except ConnectionRefusedError:
        print("Connection to server refused.")
        send_data_to_server = False
    except TimeoutError:
        print("Connection to server timed out.")
        send_data_to_server = False
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        send_data_to_server = False



# Function to send SMS message using Twilio API
def sendmessage(message):
    message = client.messages.create(
    body=message,
    from_="+18449043320",  # Twilio phone number assigned to the account
    to="+13198550756")  # recipient's phone number
    print(message.sid)


# Function to read the raw temperature data from the device file
def read_temp_raw():
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines


# Function to parse the temperature value from the device file
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

connect_to_server(current_ip,port)

# Loop to continuously read and display the temperature value
while True:
    #display.lcd_clear()
    temp_c = read_temp()
    # Check if the temperature is too low or too high
    if(temp_c <MIN_TEMP):
        sendmessage('The current temperature of {} C is too low'.format(temp_c))
    if(temp_c > MAX_TEMP):
        sendmessage('The current temperature of {} C is too high'.format(temp_c))
    # Print the temperature value to the console
    print(temp_c)
    print(type(temp_c))
    # Insert the temperature value into the database
    cursor.execute("INSERT INTO temperature (temp_c) VALUES (?);", (temp_c,))
    conn.commit()
    if(send_data_to_server):
        try:
            sock.sendall('{:.2f}'.format(temp_c).encode('utf-8'))
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            print('Disconnected from server')
            send_data_to_server = False 
    else:
        time.sleep(1)
        connect_to_server(current_ip,port)
    time.sleep(1)  # Wait for 1 second before reading the temperature again
