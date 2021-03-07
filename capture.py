import picamera
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

redpin = 16



camera = picamera.PiCamera()
camera.resolution = (3280, 2464)
GPIO.setmode(GPIO.BCM)
GPIO.setup(redpin, GPIO.OUT)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
image_number = 0

while True:
    if GPIO.input(26) == GPIO.HIGH:
        image_name = 'image{0:04d}.jpg'.format(image_number)
        camera.capture(image_name)
        image_number += 1

while TRUE:
    if GPIO.input(26) == 1 and time(1):
       camera.start_recording('videoexample.h264')
       time.sleep(5)
       camera.stop_recording
       GPIO.output(redpin, GPIO.HIGH)


    else:
        GPIO.output(ledpin, GPIO.LOW)
