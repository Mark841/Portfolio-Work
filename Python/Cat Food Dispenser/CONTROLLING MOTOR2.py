import RPi.GPIO as GPIO
import time
from time import sleep

count = 0

while count != 25201:
    if count == 25200:
        GPIO.setmode(GPIO.BOARD)

        Motor1A = 16
        Motor1B = 18
        Motor1E = 22

        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)

        print ("Turning motor on")
        print ("Going forwards")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)

        sleep(2)

        print ("Going backwards")
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)

        sleep(2)

        print ("Stopping motor")
        GPIO.output(Motor1E,GPIO.LOW)

        GPIO.cleanup()
        count = 0
    else:
        count += 1
        time.sleep(1)
    
        

