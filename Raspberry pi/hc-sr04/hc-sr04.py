import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPO21
TRIG = 21

# GPO26
ECHO = 26

# GPO20, GPO16, GP012
GREEN = 20
YELLOW = 16
RED = 12

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

# region functions
def light_green_led():
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.LOW)

def light_yellow_led():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)

def light_red_led():
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(YELLOW, GPIO.LOW)
    GPIO.output(RED, GPIO.HIGH)

def distance_senor_triggered():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end - start

    distance = sig_time / 0.000058

    print('Distance: {} centimeters'.format(distance))

    return distance

def close_or_far_led_triggered(distance):
    if distance >= 30:
        light_green_led()
    elif distance >= 20:
        light_yellow_led()
    elif distance >= 10:
        light_red_led()
    else:
        leds = [GREEN, YELLOW, RED]

        for i, led in enumerate(leds):
            GPIO.output(led, GPIO.LOW)
# endregion

while True:
    distance = distance_senor_triggered()

    close_or_far_led_triggered(distance)

    time.sleep(1)