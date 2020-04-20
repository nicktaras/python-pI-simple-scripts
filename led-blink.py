#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

# Toggles an output pin on and off for 500 milliseconds, 50 times.

# Adjust this value to match the GPIO Pin you wish to toggle the power of (on and off)
led = 7

# Initialise GPIO
GPIO.setmode(GPIO.BOARD)

# Initialise the Pin
GPIO.setup(led, GPIO.OUT)

# Toggle led or component connected to the Pin on and off 50 times
for i in range(50):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.5)

# Clean up once the program is complete (tip: it is bad practice to use this method at the start of a script)
GPIO.cleanup()
