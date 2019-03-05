import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
 
SIG_PIN = 24
GPIO.setup(SIG_PIN, GPIO.IN)

try:
	while(True):
		pressed =  GPIO.input(SIG_PIN)
		if pressed:
			print ("pressed")
			time.sleep(0.1)
except KeyboardInterrupt:
	print("Finished")
finally:
	GPIO.cleanup()
