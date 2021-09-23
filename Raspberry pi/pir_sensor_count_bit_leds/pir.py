import RPi.GPIO as GPIO
import sys
import signal
import time

# region bits explanation example
# Binaire waardes per stap. Lees van rechts naar links.
# 128 - 64 - 32 - 16 - 8 - 4 - 2 - 1

# Binaire getallen per stap. Hierboven staat hoe je het omrekend.
# 0 - 1 - 0 - 1 - 0 - 1 - 1 = 75

# 2 tot de macht positie lampje, zodat je de positie in binair kan bepalen. Hiermee kan je tellen.
# endregion

# GPO21
PIR = 21

# GPO20, GPO16, GP012, GPO25, GPO24
leds = [20, 16, 12, 25, 24]

countMovement = 0

# region functions
def pir_triggered(pin):
    global countMovement

    if GPIO.input(pin):
        countMovement += 1

        # If led bits do not exceed max count yet.
        if countMovement < (2 ** len(leds)):
            for i, led in enumerate(leds):
                bit = get_bit(countMovement, i)

                GPIO.setup(led, GPIO.OUT)

                print(bit)

                if bit > 0:
                    GPIO.output(led, GPIO.HIGH)
                else:
                    GPIO.output(led, GPIO.LOW)
        else:
            countMovement = 0

            for i, led in enumerate(leds):
                GPIO.setup(led, GPIO.OUT)

                GPIO.output(led, GPIO.LOW)
            
            print('Reset bits')

    else:
        print('No movement detected')

def get_bit(value, bit_index):
     return value & (1 << bit_index)
# endregion

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PIR, GPIO.IN)
GPIO.add_event_detect(PIR, GPIO.BOTH, callback=pir_triggered)

signal.pause()