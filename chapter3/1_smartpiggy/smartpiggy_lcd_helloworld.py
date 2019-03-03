from RPLCD.i2c import CharLCD
import time

lcd = CharLCD(i2c_expander='PCF8574', address=0x3f, charmap='A00', backlight_enabled=False)
lcd.clear();
lcd.write_string('Hello ^o^!');
while True:
	lcd.backlight_enabled = not lcd.backlight_enabled
	time.sleep(1)
