import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup( 18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup( 23, GPIO.OUT)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print("Button Pressed")
        GPIO.output(23, 1)
    else:
        GPIO.output(23,0)
    time.sleep(0.5)
