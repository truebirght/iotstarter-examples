import Adafruit_DHT

def get_humidity_temperature(pin=23):
	humidity = temperature = None

	while (humidity is None and temperature is None):
		humidity , temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)
	return humidity , temperature
