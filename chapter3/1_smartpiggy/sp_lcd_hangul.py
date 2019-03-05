from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x3f)
lcd.clear();

i = (
	0b00000,
	0b00000,
	0b00010,
	0b11011,
	0b11010,
	0b00010,
	0b00000,
	0b00000
)
lcd.create_char(0, i)

e = (
	0b00000,
	0b00000,
	0b00010,
	0b11010,
	0b11010,
	0b00010,
	0b00000,
	0b00000
)
lcd.create_char(1, e)

t = (
	0b00001,
	0b11101,
	0b10001,
	0b11101,
	0b10001,
	0b11101,
	0b00001,
	0b00000
)
lcd.create_char(2, t)

lcd.write_string('Hello \x00\x01\02')
