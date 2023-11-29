#!/usr/bin/env python3

import threading

def race_car(name):
    for circle in range(1, 1000):
        print("{} is on circle {}".format(name, circle))

# Create two threads for two cars
car1_thread = threading.Thread(target=race_car, args=['one'])
car2_thread = threading.Thread(target=race_car, args=['two'])

# Start the race
car1_thread.start()
car2_thread.start()
