import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
ledPinOne = 12
ledPinTwo = 13
GPIO.setup(ledPinOne, GPIO.OUT)
GPIO.setup(ledPinTwo, GPIO.OUT)
try:
    while True:
        GPIO.output(ledPinOne, GPIO.HIGH)
        GPIO.output(ledPinTwo, GPIO.LOW)
        time.sleep(1)
        GPIO.output(ledPinOne, GPIO.LOW)
        GPIO.output(ledPinTwo, GPIO.HIGH)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting program\n")
    GPIO.cleanup()
    exit()
        