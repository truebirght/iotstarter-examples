import af_servo as servo
import RPi.GPIO as GPIO

try:
	servo.open();
finally:
	GPIO.cleanup();
