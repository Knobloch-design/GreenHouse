import RPi.GPIO as GPIO    # Import the RPi.GPIO library to use GPIO pins
import time                # Import the time library to use sleep function
import drivers             # Import the custom drivers module
import sqlite3             # Import the SQLite library to interact with a database
import requests


global backlight_status
global url
url = "http://172.23.8.137:5000/"
backlight_status = 0

display = drivers.Lcd()
display.lcd_backlight(0)  # Turn off the display backlight
conn = sqlite3.connect('temperature.db')  # Connect to the SQLite database named 'temperature.db'

GPIO.setmode(GPIO.BCM)     # Set the pin numbering mode to BCM
GPIO.setwarnings(False)    # Disable warnings
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set up GPIO pin 26 as input with pull-up resistor

bounceTime = 200           # Set the debounce time to 200 milliseconds
def displayTemp(current_temp):  # Define a function to display the temperature on the LCD screen
    # if(!LCD_On):
    #print('CTemp ' + current_temp)
    #getTemp()
    turn_on_backlight()
    display.lcd_display_string('Temp:{} C'.format(current_temp),1)  # Display the current temperature on line 1 of the screen
    #time.sleep(.25)


def getTemp():             # Define a function to get the current temperature from the database
    #conn = sqlite3.connect('temperature.db')
    query = 'SELECT temp_c FROM temperature ORDER BY Id DESC LIMIT 1;'  # Select the most recent temperature from the database
    c = conn.cursor()
    c.execute(query)
    data = c.fetchone()    # Fetch the result
    return(data[0])        # Return the current temperature
def getTemp_all():             # Define a function to get the current temperature from the database
    #conn = sqlite3.connect('temperature.db')
    query = 'SELECT temp_c FROM temperature ORDER BY Id DESC LIMIT 300;'  # Select the most recent temperature from the database
    c = conn.cursor()
    c.execute(query)
    data = c.fetchall()    # Fetch the result
    return(pickle.dumps(data))  

def turn_on_backlight():
    data = {
    "value": True}

    response = requests.post("http://172.23.8.137:5000/", json=data)

def turn_off_backlight():
    data = {
    "value": False}
    response = requests.post("http://172.23.8.137:5000/", json=data)


# Return the current temperature
while True:                # Main program loop
    current_temp = getTemp()  # Get the current temperature from the database
    time.sleep(.1)         # Sleep for 100 milliseconds
    if(GPIO.input(26) == GPIO.LOW):  # Check if the button is pressed
        while(GPIO.input(26) == GPIO.LOW):  # Wait for the button to be released
            #displayTemp(getTemp())         # Display the temperature on the screen
            turn_on_backlight()
            print("ON")
        display.lcd_clear()    # Clear the screen when the button is released
    #display.lcd_backlight(0)     
    turn_off_backlight()
    print("OFF")             # Print "OFF" to the console at the end of each loop iteration

