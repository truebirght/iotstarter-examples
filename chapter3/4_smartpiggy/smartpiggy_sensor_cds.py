import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()

def get_light_status():
	light_val = adc.read_adc(0)
	return True if(light_val < 20000) else False;