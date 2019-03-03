import time
import RPi.GPIO as GPIO
from modules import sp_rgbled as led
from modules.sp_rgbled import Colors 
GPIO.setmode(GPIO.BCM)
  
SIG_PIN = 24
GPIO.setup(SIG_PIN, GPIO.IN)

 beforePressed = False
 
 try:
	 color_list = [Colors.BLUE, Colors.GREEN, Colors.RED, Colors.WHITE]
	 cnt = 0
	 
	 while True:
		 pressed =  GPIO.input(SIG_PIN)
		 if pressed == True and beforePressed == False:
			 cnt += 1
			 sel_color  = color_list[cnt % len(color_list)]
			 led.turnOn(sel_color)
			 print ("Led TurnOn : " + str(sel_color))
		 
		 beforePressed = pressed
		 time.sleep(0.1)
				 
 except KeyboardInterrupt:
	 print("Finished")
 finally:
	 GPIO.cleanup()
