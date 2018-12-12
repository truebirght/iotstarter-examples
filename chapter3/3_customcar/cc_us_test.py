from hcsr04sensor import sensor
import time

trig_pin = 22
echo_pin = 23

while True:
	value = sensor.Measurement(trig_pin, echo_pin)
	raw_measurement = value.raw_distance()
	metric_distance = value.distance_metric(raw_measurement)
	print(" {}cm".format(metric_distance))
