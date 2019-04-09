DEBUG = True

import time
if DEBUG:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)

    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)

    LIGHT = True

def light_on():
    if DEBUG:
        GPIO.output(22, True)
        GPIO.output(23, False)
    else:
        return True


def light_off():
    if DEBUG:
        LIGHT = False
        GPIO.output(22, False)
        GPIO.output(23, False)
    else:
        return True


def light_interval(interval):
    if DEBUG:
        sec = interval
        for i in range(100):
            time.sleep(sec)
            GPIO.output(22, True)
            time.sleep(sec)
            GPIO.output(22, False)
    else:
        return True

