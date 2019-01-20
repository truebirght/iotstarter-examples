import RPi.GPIO as GPIO
import time

IN_1 = 6
IN_2 = 13
IN_3 = 19
IN_4 = 26

GPIO.setmode(GPIO.BCM);
GPIO.setup(IN_1, GPIO.OUT);
GPIO.setup(IN_2, GPIO.OUT);
GPIO.setup(IN_3, GPIO.OUT);
GPIO.setup(IN_4, GPIO.OUT);

try:
	#모터A 전진
	GPIO.output(IN_1, 1);
	time.sleep(10);
	#모터 A 후진
	GPIO.output(IN_1, 0);
	GPIO.output(IN_2, 1);
	time.sleep(10);
	GPIO.output(IN_2, 0);
	#모터 B 전진
	GPIO.output(IN_3, 1);
	time.sleep(10);
	#모터 B 후진
	GPIO.output(IN_3, 0);
	GPIO.output(IN_4, 1);
	time.sleep(10);

except KeyboardInterrupt:
	print("Finished");
finally:
	GPIO.output(IN_1, 0);
	GPIO.output(IN_2, 0);
	GPIO.output(IN_3, 0);
	GPIO.output(IN_4, 0);
	GPIO.cleanup();
