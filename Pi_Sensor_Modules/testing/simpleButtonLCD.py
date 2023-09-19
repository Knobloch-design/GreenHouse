import RPi.GPIO as GPIO
import time
import drivers
import sqlite3
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

def displayTemp(ev=None):
   # if(!LCD_On):
    #print('CTemp ' + current_temp)
    #getTemp()
    display.lcd_on()
    display.lcd_backlight(1)
    display.lcd_display_string('Temp:{} C'.format(current_temp),1) 
    #time.sleep(.25)
def displayOFF(ev = None):
   # display.lcd_clear() 
    #display.lcd_display_string('                                    ',1) 
    display.lcd_backlight(0)
    
def getTemp():
    #conn = sqlite3.connect('temperature.db')
    query = 'SELECT temp_c FROM temperature ORDER BY Id DESC LIMIT 1;'
    c = conn.cursor()
    c.execute(query)
    data = c.fetchone() 
    return(data[0])
#GPIO.add_event_detect(26, GPIO.FALLING, callback=displayOFF, bouncetime=bounceTime)
#GPIO.add_event_detect(26, GPIO.RISING, callback=displayTemp, bouncetime=bounceTime)

while True:
    current_temp =getTemp()
    time.sleep(.1)
    if(GPIO.input(26) == GPIO.LOW):
        while(GPIO.input(26) == GPIO.LOW):
            current_temp =getTemp()
            displayTemp()
            print("ON")
        display.lcd_clear()
    #displayOFF()
    display.lcd_backlight(0)
    #display.lcd_off()
    print("OFF")
