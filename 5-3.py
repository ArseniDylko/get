import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)];
def voltage(value):
    return 3.3 * value / 256;
def setleds(value):
    setleds = [0]*8
    end = int(8*value/256)
    for i in range(0, end):
            setleds[7 - i] = 1
    return setleds

def adc():
    dec = 0
    for i in range (7, -1, -1):
        dec += 2**i
        GPIO.output(dac, decimal2binary(dec))
        time.sleep(0.05)
        if GPIO.input(comparator) == 0:
            dec -= 2**i  

    print('voltage:' + str("%.2f" % voltage(dec))+ 'V -->' + str(decimal2binary(dec)) + '\n')
    GPIO.output(leds, setleds(dec))


dac        = [26, 19, 13, 6, 5, 11, 9, 10]
comparator = 4
troyka     = 17
leds       = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comparator, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT)


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