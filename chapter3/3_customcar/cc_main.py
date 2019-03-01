import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import threading
from bluetooth import *
from hcsr04sensor import sensor as us
import time

### GPIO 핀 정의 ###
#모터
M_1 = 6
M_2 = 13
M_3 = 19
M_4 = 26

#초음파 센서
US_TRIG = 22
US_ECHO = 23

#전조등/좌,우 라이트 
LED_RIGHT = 21
LED_LEFT = 20
LED_FRONT = 16



### 상수 정의
MIN_LIGHT = 10000 # 전방라이트 점등 수치
MIN_BACK_DIST = 10 # 최소 후방 거리

### 전역변수 정의
light_val = 0 #
motor_FB = "N" # N / F / B (정지/전진/후진)
motor_LR = "N" # N / L / R (정지/좌회전/우회전)
back_dist = 10

#센서 객체 초기화
us_measure = us.Measurement(US_TRIG, US_ECHO)
cds_adc = Adafruit_ADS1x15.ADS1115()

def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(M_1, GPIO.OUT)
	GPIO.setup(M_2, GPIO.OUT)
	GPIO.setup(M_3, GPIO.OUT)
	GPIO.setup(M_4, GPIO.OUT)
	GPIO.setup(LED_RIGHT, GPIO.OUT)
	GPIO.setup(LED_LEFT, GPIO.OUT)
	GPIO.setup(LED_FRONT, GPIO.OUT)

def get_bt_chars():
	# 블루투스 시리얼 통신 UUID
	uuid = "00001101-0000-1000-8000-00805f9b34fb"
	# 블루투스 시리얼 통신 준
	while True:
		server_sock=BluetoothSocket( RFCOMM )
		server_sock.bind(('',PORT_ANY))
		server_sock.listen(1)
		port = server_sock.getsockname()[1]
		advertise_service( server_sock, "serial_examples", uuid)
		
		# 클라이언트가 연결될 때까지 대기
		print("스마트폰 연결 대기중")
		client_sock, client_info = server_sock.accept()
		print("스마트폰 연결 완료", client_info)
		
		while True:		  
				try:
					data = client_sock.recv(1024)
					if len(data) == 0: break
					str = data.decode('utf-8')
					if str == 'w':
						forward()
					if str == 'a':
						 left()
					if str == 's':
						stop()
					if str == 'd':
						right()
					if str == 'x':
						back()
				except IOError:
					client_sock.close()
					server_sock.close()
					break

def setMotorStatus(fb, lr):
	global motor_FB, motor_LR
	motor_FB = fb
	motor_LR = lr

def setLedStatus(pin, stat):
	GPIO.output(pin, stat)

def back():
	setMotorStatus("B",motor_LR)
	GPIO.output(M_3, 1)
	GPIO.output(M_4, 0)
	setLedStatus(LED_LEFT, True)
	setLedStatus(LED_RIGHT, True)
def forward():
	setMotorStatus("F",motor_LR)
	GPIO.output(M_3, 0)
	GPIO.output(M_4, 1)
	setLedStatus(LED_LEFT, False)
	setLedStatus(LED_RIGHT, False)
def right():
	setMotorStatus(motor_FB,"R")
	GPIO.output(M_1, 1)
	GPIO.output(M_2, 0)
	setLedStatus(LED_RIGHT, True)
def left():
	setMotorStatus(motor_FB,"L")
	GPIO.output(M_1, 0)
	GPIO.output(M_2, 1)
	setLedStatus(LED_LEFT, True)

def get_back_dist():
	while True:
		global motor_FB, back_dist
		back_dist = us_measure.raw_distance(sample_size = 11, sample_wait= 0.2)
		if motor_FB == "B" and back_dist <= MIN_BACK_DIST:
			motor_FB = "N"
			stop()

def get_light_val():
	global light_val
	while True:
		light_val = cds_adc.read_adc(0)
		if light_val <= MIN_LIGHT:
			setLedStatus(LED_FRONT,True)
		else:
			setLedStatus(LED_FRONT,False)

		time.sleep(0.5)

def stop():
	global motor_FB, motor_LR
	
	motor_FB = "N"
	motor_LR = "N"
	
	GPIO.output(M_1, 0);
	GPIO.output(M_2, 0);
	GPIO.output(M_3, 0);
	GPIO.output(M_4, 0);
	setLedStatus(LED_LEFT, False)
	setLedStatus(LED_RIGHT, False)


if __name__ == "__main__":
	init()
	t1 = threading.Thread(target=get_light_val)
	t2 = threading.Thread(target=get_back_dist)
	t3 = threading.Thread(target=get_bt_chars)
	
	t1.start()
	t2.start()
	t3.start()
	msg = ""

	while msg != "exit":
		msg = input("press ctrl + c to exit >")
