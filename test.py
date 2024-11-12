import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
#GPIO 17 = Rot, GPIO 27 = Gelb, GPIO 22 = Grün

while True:
    GPIO.output(17,True)
    time.sleep(2)
    GPIO.output(27,True)
    time.sleep(1)
    GPIO.output(17,False)
    time.sleep(1)
    GPIO.output(22, True)
    time.sleep(1)
    GPIO.output(27,False)
    GPIO.output(22,True)
    time.sleep(2)
    GPIO.output(22,False)
