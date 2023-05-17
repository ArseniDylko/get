import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)];
def voltage(value):
    return 3.3 * value / 256;
def adc():
    for i in range (256):       
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.01) 
        cmp_value = GPIO.input(comparator)
        if cmp_value == 0:
            print('voltage:' + str("%.2f" % voltage(i))+ 'V -->' + str(decimal2binary(i)) + '\n')
            return i

dac        = [26, 19, 13, 6, 5, 11, 9, 10]
comparator = 4
troyka     = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)


try:
    while (True):
        i = adc()


except KeyboardInterrupt:
    print('stoped by user\n')
except ValueError:
    print('wrong input\n')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)