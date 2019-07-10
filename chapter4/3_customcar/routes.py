import cc_main as car
import RPi.GPIO as GPIO
import threading
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    angle = request.form.get('angle')
    
    if angle == 'stop': car.stop()
    if angle == 'up': car.forward()
    if angle == 'down': car.back()
    if angle == 'left': car.left()
    if angle == 'right': car.right()
    
    return ('', 200)

if __name__ == '__main__':
    GPIO.setwarnings(False)
    try:
        car.init()
        t1 = threading.Thread(target=car.get_light_val)
        t2 = threading.Thread(target=car.get_back_dist)
        
        t1.start()
        t2.start()
        app.run(host='0.0.0.0', debug=True)
    finally:
        GPIO.cleanup()
