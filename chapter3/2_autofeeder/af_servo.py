import RPi.GPIO as GPIO
import sys
import time

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

def open():
	pwm = GPIO.PWM(pin, 50)
	pwm.start(2.5)
	time.sleep(1)

	pwm.ChangeDutyCycle(12.5)
	time.sleep(0.5)

	pwm.ChangeDutyCycle(2.5)
	time.sleep(1)
	pwm.stop()
