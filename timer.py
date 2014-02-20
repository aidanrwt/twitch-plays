import sys
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')

days = 0
hours = 0
minutes = 0
seconds = 0

clear()

while True:

    seconds += 1

    if seconds == 60:
        seconds = 0
        minutes += 1
        clear()

    if minutes == 60:
        minutes = 0
        hours += 1
        clear()

    if hours == 24:
        hours = 0
        days += 1
        clear()

    message = '\t{0:>2}d {1:>2}h {2:>2}m {3:>2}s\r'.format(days, hours, minutes, seconds)
    
    sys.stdout.write(message)
    sys.stdout.flush()

    time.sleep(1)