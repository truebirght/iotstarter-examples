import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
 
SIG_PIN = 17
GPIO.setup(SIG_PIN, GPIO.IN)
  
while True:
    pressed =  GPIO.input(SIG_PIN)
    if pressed:
        print ("pressed")
        time.sleep(0.1)
