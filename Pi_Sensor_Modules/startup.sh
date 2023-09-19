cd ~/seniordesign/lab_1 &
python3 sql_test.py 1> sql.log 2>&1 &
python3 wait_2.py &
job_id=$!
wait $job_id
python3 readTemp.py 1> temp.log  2>&1 &
python3 lcdDisplay.py 1> lcd.log  2>&1 & 

