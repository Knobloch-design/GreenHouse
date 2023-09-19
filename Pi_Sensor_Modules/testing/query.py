import time
import sqlite3

# Connect to the database
conn = sqlite3.connect('temperature.db')
c = conn.cursor()

# Define the query
query = 'SELECT * FROM temperature'

# Loop forever
while True:
    # Execute the query
    c.execute(query)

    # Print the results
    for row in c:
        print(row)

    # Wait for 1 second
    time.sleep(10)

# Close the connection
conn.close()
