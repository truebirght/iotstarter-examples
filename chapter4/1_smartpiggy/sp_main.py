from datetime import datetime, timedelta
import time
import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
import sp_dht11 as dht11
import sp_rgbled as led
from sp_rgbled import Colors

TOUCH_SIG_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_SIG_PIN, GPIO.IN)

lcd = CharLCD('PCF8574', 0x27)
fmt = "{0}\n\r{1[1]}C/{1[0]}%"
beforePressed = False
lastDttm = datetime.now() - timedelta(seconds=120)

try:
	color_list = [Colors.BLUE, Colors.GREEN, Colors.RED, Colors.WHITE]
	cnt = 0

	while True:
		pressed =  GPIO.input(TOUCH_SIG_PIN)

		if pressed == True and beforePressed == False:
			cnt += 1
			if cnt % 5 == 0:
				led.turnOff()
			else :
				sel_color  = color_list[cnt % len(color_list)]
				led.turnOn(sel_color)

			beforePressed = pressed
			time.sleep(0.1)

		if datetime.now() - lastDttm > timedelta(seconds=60):
			lastDttm = datetime.now()
			dtFmt = lastDttm.strftime("[%Y%m%d %H:%M]")
			str = fmt.format(dtFmt,dht11.get_humidity_temperature())
			lcd.clear()
			lcd.write_string(str)


except KeyboardInterrupt:
	print("Finished")
finally:
	GPIO.cleanup()

