import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)];
def voltage(value):
    return 3.3 * value / 256;

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

try:
    while (True):
        num = input('input a number 0-255\n')
        if num == 'q':
            print('exited by user\n')
            break;
        num = int(num)
        if num < 0 or num >= 256:
            print('wrong input\n')
            continue;
        GPIO.output(dac, decimal2binary(num))
        print('expected voltage (Volts) =', voltage(num))
except KeyboardInterrupt:
    print('stoped by user\n')
except ValueError:
    print('wrong input\n')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)