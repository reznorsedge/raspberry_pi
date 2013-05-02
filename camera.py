#!/usr/bin/python
import time
import os
import subprocess
import RPi.GPIO as GPIO
import logging
import argparse


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
        self.log = logging.getLogger('time_lapse.Motor')
        self.log.info('Create the Motor Object')
        self.log.debug('Use BCM GPIO references instead of physical pin nums')
        GPIO.setmode(GPIO.BCM)

        self.log.debug('Define GPIO signals to use pins 11, 12, 13, and 15. On'
                ' the Raspberry Pi these are GPIO17,GPIO18,GPIO27 and GPIO22.')
        self.StepPins = [17, 18, 27, 22]

        self.log.debug('Set all the pins as outputs')
        for pin in self.StepPins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        self.log.debug('Define a simple sequence.')
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
        self.log.info('Rotate %i degrees clockwise' % (number_of_degrees))
        num_iterations = number_of_degrees * 6
        StepCounter = 0

        for _ in xrange(num_iterations):
            for pin in range(0, 4):
                xpin = self.StepPins[pin]
                if self.Seq[StepCounter][pin] != 0:
                    self.log.debug('Step %i Enable %i' % (StepCounter, xpin))
                    GPIO.output(xpin, GPIO.HIGH)
                else:
                    GPIO.output(xpin, GPIO.LOW)
            StepCounter += 1

            self.log.debug("If we've reached the end of the sequence,"
                    "start again!")
            if (StepCounter == self.StepCount):
                StepCounter = 0
            if (StepCounter < 0):
                self.log.warning('How did StepCounter become lower than 0?')
                StepCounter = self.StepCount

            self.log.debug('Wait before the next step in the sequence')
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
        self.log.info('Rotate %i degress anticlockwise' % (number_of_degrees))
        num_iterations = number_of_degrees * 6
        StepCounter = 3

        for _ in xrange(num_iterations):
            for pin in range(0, 4):
                xpin = self.StepPins[pin]
                if self.Seq[StepCounter][pin] != 0:
                    self.log.debug('Step %i Enable %i' % (StepCounter, xpin))
                    GPIO.output(xpin, GPIO.HIGH)
                else:
                    GPIO.output(xpin, GPIO.LOW)
            StepCounter -= 1

            self.log.debug("If we've reached the end of the sequence, "
                    "start again!")

            if (StepCounter == -1):
                StepCounter = self.StepCount - 1
            if (StepCounter < 0):
                self.log.warning('How did StepCounter become lower than 0?')
                StepCounter = 0
            if (StepCounter > 3):
                self.log.warning('How did StepCounter become higher than 4?')
                StepCounter = self.StepCount - 1

            self.log.debug('Wait before the next step in the sequence')
            time.sleep(wait_time)


class Camera:
    def __init__(self):
        self.log = logging.getLogger('time_lapse.Camera')

    def take_photo(self, iteration, output_dir):
        self.log.debug('Take a picture. Iteration "%s"' % (iteration))
        output_file = output_dir + "/" + str(iteration).zfill(4) + ".jpg"
        subprocess.call(["fswebcam", "--save", output_file, "-r", "1280x720",
                "-q", "-d", "v4l2:/dev/video0", "-S", "15"])
        iteration += 1

    def create_film(self, output_dir):
        output_file = output_dir + "/time_lapse.avi"
        self.log.info('Create a video')
        self.log.debug("Running command with output dir: %s output file: %s"
                % (output_dir, output_file))
        subprocess.call(["mencoder", "mf://%s/*.jpg" % (output_dir), "-mf",
                "fps=24:type=jpg", "-ovc", "lavc", "-lavcopts",
                "vcodec=mpeg4:mbd=2:trell", "-oac", "copy", "-o", output_file])

def main():
    parser = argparse.ArgumentParser(description='Gather settings for time '
                                     'lapse recordings')
    parser.add_argument('-l', '--length', help='Length in minutes for the '
                        'program to run for.', type=int)
    
    args = parser.parse_args()
    
    
    
    
    output_dir = str(time.strftime("%y%m%d%H%M%S"))
    print "Making directory %s NOW" % output_dir
    # TODO: Be wary of exceptions here
    # TODO: update path as was.
    os.mkdir(output_dir)

    print 'Setup logging here'
    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(name)-18s %(levelname)-8s %(message)s',
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
    time_to_run_mins = 1
    delay_between_shots = 10
    turn_clockwise = True
    arc_to_rotate = 90

    current_angle = arc_to_rotate / 2
    timenow = time.time()
    start_time = time.time()
    time_to_finish = timenow + (time_to_run_mins * 60)
    iteration = 0

    my_motor = Motor()
    photophoto = Camera()
    log.info('TIME: Start Time: %s' % time.strftime('%Y-%m-%d %H:%M:%S',
             time.localtime(timenow)))
    while timenow < time_to_finish:
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

    photography_end_time = time.time()
    log.info('TIME: End of photography time: %s' %
             time.strftime('%Y-%m-%d %H:%M:%S',
             time.localtime(photography_end_time)))
    photophoto.create_film(output_dir)
    video_end_time = time.time()
    log.info('TIME: End of create video: %s' % 
             time.strftime('%Y-%m-%d %H:%M:%S',
             time.localtime(video_end_time)))

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

    motor_move_end_time = time.time()
    log.info('TIME: End of rotate motor back to start: %s' % 
             time.strftime('%Y-%m-%d %H:%M:%S',
             time.localtime(motor_move_end_time)))

    start_time_nice = time.strftime('%H:%M:%S', time.localtime(start_time))
    photography_end_time_nice = time.strftime(
            '%H:%M:%S', time.localtime(photography_end_time))
    time_to_finish_nice = time.strftime(
            '%H:%M:%S', time.localtime(time_to_finish))
    video_end_time_nice = time.strftime(
            '%H:%M:%S', time.localtime(video_end_time))
    motor_move_end_time_nice = time.strftime(
            '%H:%M:%S', time.localtime(motor_move_end_time))

    log.info('+-------------------------------------+')
    log.info(
             '| Start time    | %s |          |' % (start_time_nice))
    log.info(
             '| Photos end    | %s | %s |' % (photography_end_time_nice,
             time.strftime('%H:%M:%S', time.localtime(
             (photography_end_time - start_time)))))
    log.info(
             '| Requested end | %s | %s |' % (time_to_finish_nice,
             time.strftime('%H:%M:%S', time.localtime(
             photography_end_time - time_to_finish))))
    log.info(
             '| Video created | %s | %s |' % (video_end_time_nice,
             time.strftime('%H:%M:%S', time.localtime(
             video_end_time - time_to_finish))))
    log.info(
             '| Motor moved   | %s | %s |' % (motor_move_end_time_nice,
             time.strftime('%H:%M:%S', time.localtime(
             motor_move_end_time - video_end_time))))
    log.info(
             '| Overall time  |          | %s |' % (
             time.strftime('%H:%M:%S', time.localtime(
             motor_move_end_time - start_time))))
    log.info('+-------------------------------------+')
    log.info('And we are DONE!')


if __name__ == "__main__":
    main()
