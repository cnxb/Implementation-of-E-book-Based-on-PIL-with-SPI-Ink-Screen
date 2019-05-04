import os
import RPi.GPIO as GPIO
pin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
while True:
    if GPIO.input(pin) == 1:
        os.system('python read.py')
