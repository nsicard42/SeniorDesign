import RPi.GPIO as GPIO
import time as time

#this script shows all the different combinations of GPIO outputs  from the raspberry pi
#the intent is to show that by interacting with GPIO we can control the RC car

GPIO.setmode(GPIO.BCM)

GPIO_FORWARD = 18
GPIO_REVERSE= 23
GPIO_LEFT = 24
GPIO_RIGHT = 25

GPIO.setup(GPIO_FORWARD, GPIO.OUT)
GPIO.setup(GPIO_REVERSE, GPIO.OUT)
GPIO.setup(GPIO_LEFT, GPIO.OUT)
GPIO.setup(GPIO_RIGHT, GPIO.OUT)

def autopilet():
    GPIO.output(GPIO_FORWARD, True)
    time.sleep(1)
    GPIO.output(GPIO_LEFT, True)
    time.sleep(1)
    GPIO.output(GPIO_LEFT, False)
    GPIO.output(GPIO_RIGHT, True)
    time.sleep(1)
    GPIO.output(GPIO_FORWARD, False)
    GPIO.output(GPIO_REVERSE,True)
    time.sleep(1)
    GPIO.output(GPIO_LEFT, True)
    GPIO.output(GPIO_RIGHT, False)
    time.sleep(1)
    GPIO.output(GPIO_REVERSE, False)
    GPIO.output(GPIO_LEFT, False)
    return 1
    
    
if __name__ == '__main__':
    try:
        while True:
            autopilet()
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
            print("Mautopilot stopped")
            GPIO.cleanup()
