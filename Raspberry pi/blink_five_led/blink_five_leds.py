import RPi.GPIO as GPIO
import time

# GPO21, GPO16, GP012, GPO25, GPO24
leds = [21, 16, 12, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

while True:
    for i, led in enumerate(leds):
        GPIO.setup(led, GPIO.OUT)
        
        GPIO.output(led, GPIO.HIGH)

        time.sleep(0.5)

        GPIO.output(led, GPIO.LOW)