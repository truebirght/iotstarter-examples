import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
  
SIG_PIN = 24
GPIO.setup(SIG_PIN, GPIO.IN)

beforePressed = False

try:
	while True:
		pressed =  GPIO.input(SIG_PIN)
		if pressed == True and beforePressed == False:
			print ("touched")
			
		beforePressed = pressed
		time.sleep(0.1)
				 
except KeyboardInterrupt:
	print("Finished")
finally:
	GPIO.cleanup()
