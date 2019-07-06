import RPi.GPIO as GPIO
import time

PIN_BLUE=16
PIN_GREEN=20
PIN_RED=21

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_BLUE, GPIO.OUT)
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setup(PIN_RED, GPIO.OUT)

def turnOff():
	GPIO.output(PIN_BLUE,0);
	GPIO.output(PIN_GREEN,0);
	GPIO.output(PIN_RED,0);

def turnOn(pin):
	GPIO.output(pin,1);

while(True):
	turnOff();
	turnOn(PIN_BLUE);
	time.sleep(3);
	
	turnOff();
	turnOn(PIN_GREEN);
	time.sleep(3);
	
	turnOff();
	turnOn(PIN_RED);
	time.sleep(3);

	turnOff();
	turnOn(PIN_BLUE);
	turnOn(PIN_GREEN);
	turnOn(PIN_RED);
	time.sleep(3);
	


