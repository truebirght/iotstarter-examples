import time
import RPi.GPIO as GPIO
from modules import af_servo as servo

GPIO.setmode(GPIO.BCM)

SIG_PIN = 20;
GPIO.setup(SIG_PIN, GPIO.IN)

beforePressed = False

try:
	while(True):
		pressed = not GPIO.input(SIG_PIN)
		if pressed and beforePressed == False:
			print ("servo open");
			servo.open();
		
		beforePressed = pressed;
		time.sleep(0.1);
except KeyboardInterrupt:
	print("Finished");
finally:
	GPIO.cleanup();
