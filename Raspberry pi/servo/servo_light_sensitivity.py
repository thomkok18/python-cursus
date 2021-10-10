import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import time

# The sensitivity of the analog reads.
GAIN = 1
ANALOG_PORT = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
servo = GPIO.PWM(21, 50)    # 50Hz

# Choose either one.
# adc = Adafruit_ADS1x15.ADS1015() # 12 bit
adc = Adafruit_ADS1x15.ADS1115() # 16 bit
adc.start_adc(ANALOG_PORT, gain=GAIN)
time.sleep(0.1) # Give the chip score time.

servo.start(7.5)
time.sleep(0.5)

while True:
    value = adc.get_last_result()

    print(value)

    if value >= 0:
        servo.ChangeDutyCycle(10)
    else:
        servo.ChangeDutyCycle(5)

    time.sleep(0.1)