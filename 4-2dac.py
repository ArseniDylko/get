import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)];
def voltage(value):
    return 3.3 * value / 256;

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

try:
    while (True):
        for i in range (0,255):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(0.02)
        for i in range (0,255):
            GPIO.output(dac, decimal2binary(255 - i))
            time.sleep(0.02)
except KeyboardInterrupt:
    print('stoped by user\n')
except ValueError:
    print('wrong input\n')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)