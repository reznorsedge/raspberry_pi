#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
import logging

log = logging.getLogger('motor_rotate')


class Motor:

    def __init__(self):
        '''Define a motor instance. Help taken from:

        Matt Hawkins website and cold mostly taken from there.
        http://www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/

        Other useful links:
        http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
        http://www.raspberrypi-spy.co.uk/2012/09/checking-your-raspberry-pi-board-version/
        http://www.scraptopower.co.uk/Raspberry-Pi/how-to-connect-stepper-motors-a-raspberry-pi
        http://www.adafruit.com/blog/2013/01/23/adafruits-raspberry-pi-lesson-10-stepper-motors-raspberry_pi-raspberrypi/
        '''
        log = logging.getLogger('motor.Motor')
        log.info('Create the Motor Object')
        log.debug('Use BCM GPIO references instead of physical pin nums')
        GPIO.setmode(GPIO.BCM)

        log.debug('Define GPIO signals to use pins 11, 12, 13, and 15. On'
                ' the Raspberry Pi these are GPIO17,GPIO18,GPIO27 and GPIO22.')
        self.StepPins = [17, 18, 27, 22]

        log.debug('Set all the pins as outputs')
        for pin in self.StepPins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        log.debug('Define a simple sequence.')
        # TODO: Understand this, and if necessary update it.
        self.StepCount = 4
        self.Seq = []
        self.Seq = range(0, self.StepCount)
        self.Seq[0] = [1, 0, 0, 0]
        self.Seq[1] = [0, 1, 0, 0]
        self.Seq[2] = [0, 0, 1, 0]
        self.Seq[3] = [0, 0, 0, 1]

    def rotate_clockwise(self, number_of_degrees, wait_time=0.05):
        '''
        Run through the stepper motor sequence to move it through the number of
        degrees specified.

        360 degress requires 4000 iterations. (From visual inspection)
        1 degree requires 11(.1 recurring) iterations.

        For some reason I don't understand I needed to half that number

        :param number_of_degrees: Number of degress you wish the motor to
            rotate. Naturally 360 would be a complete circle.
        :param wait_time: The amount of time to wait between steps. Too fast
            and it may not actually turn. Default 0.05.
        '''
        log.info('Rotate %i degrees clockwise' % (number_of_degrees))
        num_iterations = number_of_degrees * 6
        StepCounter = 0

        for _ in xrange(num_iterations):
            for pin in range(0, 4):
                xpin = self.StepPins[pin]
                if self.Seq[StepCounter][pin] != 0:
                    log.debug('Step %i Enable %i' % (StepCounter, xpin))
                    GPIO.output(xpin, GPIO.HIGH)
                else:
                    GPIO.output(xpin, GPIO.LOW)
            StepCounter += 1

            log.debug("If we've reached the end of the sequence, start again!")
            if (StepCounter == self.StepCount):
                StepCounter = 0
            if (StepCounter < 0):
                log.warning('How did StepCounter become lower than 0?')
                StepCounter = self.StepCount

            log.debug('Wait before the next step in the sequence')
            time.sleep(wait_time)

    def rotate_anticlockwise(self, number_of_degrees, wait_time=0.05):
        '''
        Run through the stepper motor sequence to move it through the number of
        degrees specified.

        360 degress requires 4000 iterations. (From visual inspection)
        1 degree requires 11(.1 recurring) iterations.

        For some reason I don't understand I needed to half that number

        :param number_of_degrees: Number of degress you wish the motor to
            rotate. Naturally 360 would be a complete circle.
        :param wait_time: The amount of time to wait between steps. Too fast
            and it may not actually turn. Default 0.05.
        '''
        log.info('Rotate %i degress anticlockwise' % (number_of_degrees))
        num_iterations = number_of_degrees * 6
        StepCounter = 3

        for _ in xrange(num_iterations):
            for pin in range(0, 4):
                xpin = self.StepPins[pin]
                if self.Seq[StepCounter][pin] != 0:
                    log.debug('Step %i Enable %i' % (StepCounter, xpin))
                    GPIO.output(xpin, GPIO.HIGH)
                else:
                    GPIO.output(xpin, GPIO.LOW)
            StepCounter -= 1

            log.debug("If we've reached the end of the sequence, start again!")

            if (StepCounter == -1):
                StepCounter = self.StepCount - 1
            if (StepCounter < 0):
                log.warning('How did StepCounter become lower than 0?')
                StepCounter = 0
            if (StepCounter > 3):
                log.warning('How did StepCounter become higher than 4?')
                StepCounter = self.StepCount - 1

            log.debug('Wait before the next step in the sequence')
            time.sleep(wait_time)


def main():
    output_dir = str(time.strftime("%y%m%d%H%M%S"))
    print "Making directory %s NOW" % output_dir
    # TODO: Be wary of exceptions here
    # TODO: update path as was.
    os.mkdir(output_dir)

    print 'Setup logging here'
    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(name)-18s %(levelname)-8s %(message)s',
            dateftm='%d-%m %H:%M',
            filename='%s/motor_full.log' % (output_dir))

    formatter = logging.Formatter('%(name)-18s: %(levelname)-8s %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    info_log = logging.FileHandler('%s/motor_info.log' % (output_dir))
    info_log.setLevel(logging.INFO)
    info_log.setFormatter(formatter)

    logging.getLogger('').addHandler(console)
    logging.getLogger('').addHandler(info_log)
    log = logging.getLogger('motor')
    my_motor = Motor()

    rotate_clockwise = raw_input('Rotate the motor clockwise? (Yes/No)?')
    degrees_rotation = raw_input('How many degress should the motor be '
            'rotated?')

    #TODO Be cleverer here.
    if 'y' in rotate_clockwise.lower():
        if type(eval(degrees_rotation)) == int:
            log.info('Rotating the motor clockwise %s degrees' % (
                    degrees_rotation,))
            my_motor.rotate_clockwise(eval(degrees_rotation))
        else:
            log.error('The type of degrees_rotation in rotate_clockwise was %s'
                    ' and the value was %s' % (type(eval(degrees_rotation)),
                    degrees_rotation))
    elif 'n' in rotate_clockwise.lower():
        if type(eval(degrees_rotation)) == int:
            log.info('Rotating the motor anti-clockwise %s degrees' % (
                    degrees_rotation,))
            my_motor.rotate_anticlockwise(eval(degrees_rotation))
        else:
            log.error('The type of degrees_rotation in rotate_anti_clockwise '
                    'was %s and the value was %s' % (
                    type(eval(degrees_rotation)), degrees_rotation))
    log.info('And we are DONE!')


if __name__ == "__main__":
    main()
