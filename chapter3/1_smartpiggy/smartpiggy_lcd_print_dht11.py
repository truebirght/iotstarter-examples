from RPLCD.i2c import CharLCD
import smartpiggy_sensor_dht11
import time

lcd = CharLCD('PCF8574', 0x3f)
while(True):
	humidity , temperature = smartpiggy_sensor_dht11.get_humidity_temperature(18)
	lcd.clear()
	print(humidity, temperature)
	lcd.write_string('Temp={0:0.1f}*\n\rHumidity={1:0.1f}%'.format(temperature, humidity))
	time.sleep(5)

