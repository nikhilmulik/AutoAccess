import time
import RPi.GPIO as GPIO

# Next we setup the pins for use!
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

LIGHT = True

def light_on():
  GPIO.output(22, True)
  GPIO.output(23, False)


def light_off():
  LIGHT = False
  GPIO.output(22, False)
  GPIO.output(23, False)


def light_interval(interval):
  t = interval
  while LIGHT:
    time.sleep(t)
    GPIO.output(22, True)
    time.sleep(t)
    GPIO.output(22, False)

