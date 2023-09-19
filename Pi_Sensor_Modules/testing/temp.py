import os
import glob
import sqlite3
import socket
import time
import drivers
import mysql.connector
# Load the necessary kernel modules
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
device_file = '/sys/bus/w1/devices/28-3c43f649c25b/w1_slave'
mydb = mysql.connector.connect(
        host= 'alectestdb.cb4kadb1h8mb.us-east-2.rds.amazonaws.com',
        user= 'alecmaliky',
        password= 'markisthegoat'
        )
cursor = mydb.cursor()
#conn = sqlite3.connect('temperature.db')
# Create a cursor object
#cursor = conn.cursor()
# Function to read the temperature from the thermocouple
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

# Loop to continuously read and display the temperature value
while True:
    #display.lcd_clear()
    temp_c = read_temp()
    print(temp_c)
    print(type(temp_c))
    cursor.execute("INSERT INTO temperature (temp_c) VALUES (?);", (temp_c,))
    conn.commit()
    time.sleep(1)
