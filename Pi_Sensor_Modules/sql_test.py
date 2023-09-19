import sqlite3
from flask import Flask, jsonify, request
import json 
app = Flask(__name__)
import drivers
global db, cursor

display = drivers.Lcd()
display.lcd_backlight(0)
global current_temp        # Declare a global variable for the current temperature
global buttonPressed       # Declare a global variable for the button state
buttonPressed=False        # Set the initial button state to False

@app.route('/temperature_300')
def temperature_300():
    db = sqlite3.connect('temperature.db')  # Connect to the SQLite database named 'temperature.db'
    cursor = db.cursor()
    cursor.execute('SELECT * FROM temperature ORDER BY id DESC LIMIT 300')
    result = cursor.fetchall()
    db.close()
    #return jsonify({'temp_c': result[1]})
    return json.dumps(result)
@app.route('/temperature')
def temperature():
    db = sqlite3.connect('temperature.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM temperature ORDER BY id DESC LIMIT 1')
    result = cursor.fetchall()
    db.close()
    #return jsonify({'temp_c': result[1]})
    return jsonify(result)

@app.route('/', methods=['POST'])
def set_lcd_backlight():
    data = request.get_json()
    print(buttonPressed)
    value = data['value']

    '''
       if not value and buttonPressed:
        print(value)
        buttonPressed = False
        display.lcd_clear()
    if value and not buttonPressed:
        buttonPressed = True
    '''
    display.lcd_backlight(value)
    if value:
        current_temp = getTemp()
        display.lcd_display_string('Temp:{} C'.format(current_temp),1)
    return "Data received successfully."

def getTemp():             # Define a function to get the current temperature from the database
    db = sqlite3.connect('temperature.db')
    cursor = db.cursor()
   #conn = sqlite3.connect('temperature.db')
    query = 'SELECT temp_c FROM temperature ORDER BY Id DESC LIMIT 1;'  # Select the most recent temperature from the databas
    cursor.execute(query)
    data = cursor.fetchone()    # Fetch the result
    return(data[0])   

if __name__ == '__main__':
    buttonPressed = False
    app.run(host='172.23.8.137', port=5000)
