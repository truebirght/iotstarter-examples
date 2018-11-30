import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
time.sleep(1)
#p.stop()
try:
  while True:
    print("2.5 start")
#    p.start(2.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(5)
#    p.stop()

#    print("7.5 start")
#    time.sleep(3)
#    p.start(7.5)
#    p.ChangeDutyCycle(7.5)
#    time.sleep(0.5)
#    p.stop()
#    print("10 start")
#    p.ChangeDutyCycle(10)
#    time.sleep(1)

    print("12.5 start")
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)

#    print("10 start")
#    p.ChangeDutyCycle(10)
#    time.sleep(0.5)

#    print("7.5 start")
#    p.ChangeDutyCycle(7.5)
#    time.sleep(0.5)

#    print("5 start")
#    p.ChangeDutyCycle(5)
#    time.sleep(0.5)
    
#    print("2.5 start")
#    p.ChangeDutyCycle(2.5)
#    time.sleep(0.5)
except KeyboardInterrupt:
  p.ChangeDutyCycle(2.5)
  time.sleep(0.5)
  p.stop()
  GPIO.cleanup()
