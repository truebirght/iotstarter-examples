import Adafruit_ADS1x15
import time

adc = Adafruit_ADS1x15.ADS1115()

while True:
    light_val = adc.read_adc(0)
    print('light val : ' + str(light_val))
    time.sleep(1)
