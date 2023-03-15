import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)];

GPIO.setmode(GPIO.BCM)

dac = [26, 22]

GPIO.setup(dac, GPIO.OUT)

p = GPIO.PWM(22, 1000)

try:
    while (True):
        duty_cycle = input('input a duty cycle value\n')
        if duty_cycle == 'q':
            print('exited by user\n')
            break;
        duty_cycle = int(duty_cycle)
        p.start(duty_cycle)
except KeyboardInterrupt:
    print('stoped by user\n')
finally:
    p.stop()
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)