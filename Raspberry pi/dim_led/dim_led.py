import RPi.GPIO as GPIO
import time

dutyCycle = 0

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
LED = GPIO.PWM(21, 100) # 100 Hertz
LED.start(dutyCycle)	# begin PWM

while True:
	dutyCycle += 1
	LED.ChangeDutyCycle(abs((dutyCycle % 200) - 100))
	time.sleep(0.01)