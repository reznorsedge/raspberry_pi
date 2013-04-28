#!/usr/bin/python
import time
import os
import subprocess
import time
import RPi.GPIO as GPIO
import logging

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
        log = logging.getLogger('camera.Motor')
        log.info('Create the Motor Object')
        log.debug('Use BCM GPIO references instead of physical pin nums')
        GPIO.setmode(GPIO.BCM)

        log.debug('Define GPIO signals to use pins 11, 12, 13, and 15. On'
                ' the Raspberry Pi these are GPIO17,GPIO18,GPIO27 and GPIO22.')
        self.StepPins = [17,18,27,22]

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

        for x in xrange(num_iterations):
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

        for x in xrange(num_iterations):
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

class Camera:

    def __init__(self):
        log = logging.getLogger('time_lapse.camera')


    def take_photo(self, iteration, output_dir):
        log.debug('Take a picture. Iteration "%s"' % (iteration))
        output_file = output_dir + "/" + str(iteration).zfill(4) + ".jpg"
        subprocess.call(["fswebcam", "--save", output_file, "-r", "1280x720", "-q", "-d", "v4l2:/dev/video0", "-D", "2"])
        #subprocess.call(["fswebcam", "--save", output_file, "-r", "1280x720", "-q", "-d", "v4l2:/dev/video0"])

        iteration += 1

    def create_film(self, output_dir):
        output_file = output_dir + "/time_lapse.avi"
        log.info('Create a video')
        log.debug("Running command with output dir: %s output file: %s" % (output_dir, output_file))
        subprocess.call(["mencoder", "mf://%s/*.jpg" %(output_dir), "-mf", "fps=24:type=jpg", "-ovc", "lavc", "-lavcopts", "vcodec=mpeg4:mbd=2:trell", "-oac", "copy", "-o", output_file])

def main():
    print "Making directory %s NOW" %output_dir
    # TODO: Be wary of exceptions here
    # TODO: update path as was.
    output_dir = "/home/pi/time_lapse" + str(time.strftime("%y%m%d%H%M%S"))
    os.mkdir(output_dir)

    print 'Setup logging here'
    logging.basicConfig(level=logging.DEBUG,
            format=%(asctime)s %(name)-18 %(levelname)-8 %(message)s,
            dateftm='%d-%m %H:%M',
            filename='%s/time_lapse_full.log' % (output_dir))

    formatter = logging.Formatter('%(name)-18s: %(levelname)-8s %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    info_log = logging.FileHandler('%s/time_lapse_info.log' % (output_dir))
    info_log.setLevel(logging.INFO)
    info_log.setFormatter(formatter)

    logging.getLogger('').addHandler(console)
    logging.getLogger('').addHandler(info_log)
    log = logging.getLogger('time_lapse')

    log.info('Top of Main')

    # 24 hours = 1440 mins
    time_to_run_mins = 1440
    delay_between_shots = 100
    turn_clockwise = True
    arc_to_rotate = 90
    timenow = time.time()

    current_angle = arc_to_rotate / 2
    timenow = time.time()
    timetofinish = timenow + (time_to_run_mins * 60)
    iteration = 0 

    my_motor = Motor()
    photophoto = Camera()

    while timenow < timetofinish:
        photophoto.take_photo(iteration, output_dir)
        timenow = time.time()
        if turn_clockwise:
            my_motor.rotate_clockwise(1)
            if current_angle >= 90:
                turn_clockwise = False
            else:
                current_angle += 1
        else:
            my_motor.rotate_anticlockwise(1)
            if current_angle <= 0:
                turn_clockwise = True
            else:
                current_angle -= 1
        iteration += 1
        time.sleep(delay_between_shots)

    photophoto.create_film(output_dir)

    log.info('Reset the motor to the start position')
    half_way = (arc_to_rotate / 2)
    if current_angle > half_way:
        log.info('Rotate anticlockwise %s steps' % (current_angle - half_way))
        my_motor.rotate_anticlockwise(current_angle - half_way)
    elif current_angle < half_way:
        log.info("rotate clockwise %s steps" % (half_way - current_angle))
        my_motor.rotate_clockwise(half_way - current_angle)
    else:
        log.info('Do not need to do anything.')

    log.info('And we are DONE!')


if __name__ == "__main__":
    main()
    
