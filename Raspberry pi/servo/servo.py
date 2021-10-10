import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
servo = GPIO.PWM(21, 50)    # 50Hz

while True:
    servo.start(7.5)            # Center
    time.sleep(0.5)
    servo.ChangeDutyCycle(10)   # Left
    time.sleep(0.5)
    servo.ChangeDutyCycle(5)    # Right
    time.sleep(0.5)

GPIO.cleanup()