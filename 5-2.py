import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)];
def voltage(value):
    return 3.3 * value / 256;
def adc():
    dec = 0
    for i in range (7, -1, -1):
        dec += 2**i
        GPIO.output(dac, decimal2binary(dec))
        time.sleep(0.05)
        if GPIO.input(comparator) == 0:
            dec -= 2**i  

    print('voltage:' + str("%.2f" % voltage(dec))+ 'V -->' + str(decimal2binary(dec)) + '\n')


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