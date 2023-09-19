import os
import glob
import socket
import time
import drivers
# Load the necessary kernel modules
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
server_address = ('172.17.103.166', 8080)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

# Define the location of the thermocouple device file
device_file = '/sys/bus/w1/devices/28-3c43f649c25b/w1_slave'
display = drivers.Lcd()
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
    data ='Temperature: {} C'.format(temp_c)
    print(data)
    display.lcd_display_string('Temp: {} C'.format(temp_c),1)
    sock.sendall(data.encode('utf-8'))
    time.sleep(1)
