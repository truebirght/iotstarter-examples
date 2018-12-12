import RPi.GPIO as GPIO
import sys
import time
import pygame

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pygame.mixer.init()
pygame.mixer.music.load("bell.mp3")
pygame.mixer.music.set_volume(1.0)

def open():
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		pass
	pwm = GPIO.PWM(pin, 50)
	pwm.start(2.5)
	time.sleep(1)

	pwm.ChangeDutyCycle(12.5)
	time.sleep(0.5)

	pwm.ChangeDutyCycle(2.5)
	time.sleep(1)
	pwm.stop()
