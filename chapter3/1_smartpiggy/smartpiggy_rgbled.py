from enum import IntEnum
import RPi.GPIO as GPIO

class Colors(IntEnum):
    BLUE = 16
    GREEN = 20
    RED = 21
    WHITE = 999

GPIO.setmode(GPIO.BCM)
GPIO.setup(Colors.BLUE, GPIO.OUT)
GPIO.setup(Colors.GREEN, GPIO.OUT)
GPIO.setup(Colors.RED, GPIO.OUT)

def turnOff():
    GPIO.output(Colors.BLUE,0);
    GPIO.output(Colors.GREEN,0);
    GPIO.output(Colors.RED,0);

def turnOn(color):
    if not isinstance(color, Colors):
        raise TypeError('반드시 Colors 매개변수를 사용하여야 합니다.');
    
    turnOff();
    if color == Colors.WHITE:
        GPIO.output(Colors.BLUE,1);
        GPIO.output(Colors.GREEN,1);
        GPIO.output(Colors.RED,1);
    else: 
        GPIO.output(color,1);

