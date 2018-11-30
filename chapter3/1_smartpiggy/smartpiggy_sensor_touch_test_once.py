import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
 
SIG_PIN = 17
GPIO.setup(SIG_PIN, GPIO.IN)

beforePressed = False

while True:
    pressed =  GPIO.input(SIG_PIN)

    if pressed == True and beforePressed == False:
        print ("touched")

    beforePressed = pressed
    time.sleep(0.1)
