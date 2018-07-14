import RPi.GPIO as GPIO
import sys
import time

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 50)

def left():
    pwm.ChangeDutyCycle(2.5)

def middle():
    pwm.ChangeDutyCycle(7.5)

def right():
    pwm.ChangeDutyCycle(12.5)


