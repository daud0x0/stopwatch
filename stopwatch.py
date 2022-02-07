#!/usr/bin/python3
# stopwatch.py      - A simple stopwatch program

import time

# Display the program instructions.
print("Press enter to begin. Afterward, press ENTER to 'click' the stopwatch. press Ctrl-c to quite")

input()         # Press enter to begin
print("Started")

startTime = time.time()      # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the time
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime,2)
        print('Lap #%s: %s (%s)' %(lapNum, totalTime, lapTime),end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-c exception to keep its error from displaying.
    print('\nDone')

