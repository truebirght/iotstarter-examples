from hcsr04sensor import sensor
import datetime

trig_pin = 22
echo_pin = 23

while True:
	value = sensor.Measurement(trig_pin, echo_pin)
	raw_measurement = value.raw_distance(sample_size = 11, sample_wait= 0.2)
	metric_distance = value.distance_metric(raw_measurement)
	print(" [{}] {}cm".format(datetime.datetime.now().strftime("%H:%M:%S"),metric_distance))
