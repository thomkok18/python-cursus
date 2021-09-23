import RPi.GPIO as GPIO
import time

# GPO21
LED = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LED, GPIO.OUT)

while True:
    GPIO.output(LED, GPIO.HIGH)

    time.sleep(0.5)

    GPIO.output(LED, GPIO.LOW)

    time.sleep(0.5)