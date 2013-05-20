#!/usr/bin/python
import time
import datetime
import os
import subprocess
import logging
import Image
import sys


class Camera:
    def __init__(self):
        self.log = logging.getLogger('time_lapse.Camera')

    def take_photo(self, iteration, output_dir):
        time_now_nice = time.strftime('%H:%M:%S', time.localtime(time.time()))
        self.log.info(
            '(%s) Take a picture. Iteration "%s"' % (time_now_nice, iteration))
        output_file = output_dir + "/" + str(iteration).zfill(4) + ".jpg"
        subprocess.call(
            ["fswebcam", "--save", output_file, "-r", "1280x720", "-q", "-d",
                "v4l2:/dev/video0", "-S", "15"])
        iteration += 1

    def create_film_from_files(
            self, source_dir, fps, output_name="time_lapse.avi"):
        '''
        Create a movie using a directory of images.
        '''
        output_file = os.path.join(source_dir, output_name)
        self.log.info('Create a video')
        self.log.debug(
            "Running command with output dir: %s output file: %s" % (
                source_dir, output_file))
        subprocess.call(
            ["mencoder", "mf://%s/*.jpg" % (source_dir), "-mf",
                "fps=%s:type=jpg" % fps, "-ovc", "lavc", "-lavcopts",
                "vcodec=mpeg4:mbd=2:trell", "-oac", "copy", "-o", output_file])

    def create_film_from_list(
            self, input_file, input_dir, output_dir, fps,
            output_name="time_lapse.avi"):
        '''
        Create a movie using a list of files inside a file.
        '''
        origWD = os.getcwd()  # remember our original working directory

        os.chdir(os.path.join(os.path.abspath(sys.path[0]), input_dir))

        output_file = os.path.join("..", output_dir, output_name)
        input_path = os.path.join(input_dir, input_file)

        self.log.info(
            'Create a video from list of filenames (%s)' % (input_path))
        self.log.info(
            'Running command with output dir "%s" and output file %s' % (
                output_dir, output_file))
        subprocess.call(
            ["mencoder", "mf://@%s" % input_file, "-mf", "fps=%s:type=jpg" %
                fps, "-ovc", "lavc", "-lavcopts", "vcodec=mpeg4:mbd=2:trell",
                "-oac", "copy", "-o", output_file])
        os.chdir(origWD)

    def analyse_files(
            self, images_location, output_dir, too_dark='too_dark.txt',
            ok_images='ok_images.txt', percent_black=96.0):
        '''
        Create two lists of files. One has the files which are deemed useful
        to the video, the other is ones to discard (i.e. too dark to be used)
        '''
        list_of_files = []
        too_dark_images_list = []
        ok_images_list = []
        too_dark_filename = os.path.join(output_dir, too_dark)
        ok_files_filename = os.path.join(output_dir, ok_images)

        self.log.debug('Build up a list of files to check')
        for files in os.listdir(images_location):
            if files.endswith('.jpg'):
                list_of_files.append(files)

        self.log.debug('Look at the histogram and put in the correct file')

        too_dark_file = open(too_dark_filename, 'w')
        ok_files_file = open(ok_files_filename, 'w')
        for target_file in list_of_files:
            image_file_name = os.path.join(images_location, target_file)
            image_file = Image.open(image_file_name)
            image_file = image_file.convert('1')
            hist = image_file.histogram()
            if (100 * (
                    float(hist[0]) / float(sum(hist)))) > float(percent_black):
                too_dark_images_list.append(target_file)
            else:
                ok_images_list.append(target_file)

        too_dark_images_list.sort()
        ok_images_list.sort()
        for target_image in too_dark_images_list:
            too_dark_file.write('%s\n' % target_image)
        for target_image in ok_images_list:
            ok_files_file.write('%s\n' % target_image)

        self.log.debug('Close the files')
        too_dark_file.close()
        ok_files_file.close()

        self.log.debug(
            'toodark: %s\n\nok: %s\n\n' % (
                too_dark_images_list, ok_images_list))
        self.log.info('Total images: %s\n'
                      'Light images: %s\n'
                      'Dark images : %s\n' % (len(list_of_files),
                      len(ok_images_list), len(too_dark_images_list)))
        return too_dark, ok_images


def main():
    output_dir = str(time.strftime("%y%m%d%H%M%S"))
    print "Making directory %s NOW" % output_dir
    # TODO: Be wary of exceptions here
    # TODO: update path as was.
    os.mkdir(output_dir)

    print 'Setup logging here'
    logging.basicConfig(
        level=logging.DEBUG,
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
    skip_photos = raw_input('Are we just making a video? (yes / no)').lower()
    fps = raw_input('How many frames per second should be do?')
    if skip_photos.startswith('y'):
        skip_photos = True
        input_dir = raw_input(
            'What is the relative path for the existing photos (e.g. '
            '130513210627)?')
        delay_between_shots = 1
        time_to_run_mins = 1
    else:
        skip_photos = False
        time_to_run_mins = int(
            raw_input(
                'How long in minutes would you like the program to run? '
                '(1440 mins = 24 hours)'))
        delay_between_shots = int(
            raw_input('What delay should there be between shots (in secs)?'))
        input_dir = output_dir

    start_time = time.time()
    start_time_nice = time.strftime('%H:%M:%S', time.localtime(start_time))

    time_to_finish = start_time + (time_to_run_mins * 60)
    time_to_finish_nice = time.strftime(
        '%H:%M:%S', time.localtime(time_to_finish))
    iteration = 0

    photophoto = Camera()

    log.info('Starting with the following parameters:\n'
             'start_time: %s (%s)\n'
             'time_to_run_mins: %s\n'
             'delay_between_shots: %s\n'
             'time_to_finish: %s (%s)\n'
             'skipping photos: %s'
             % (start_time, start_time_nice, time_to_run_mins,
                delay_between_shots, time_to_finish, time_to_finish_nice,
                skip_photos))
    timenow = time.time()
    if not skip_photos:
        while timenow < time_to_finish:
            print timenow
            photophoto.take_photo(iteration, output_dir)
            timenow = time.time()
            iteration += 1
            time.sleep(delay_between_shots)

    end_time = time.time()

    log.info('Generate lists of light and dark images')
    too_dark_2, ok_images = photophoto.analyse_files(input_dir, output_dir)

    #photophoto.create_film_from_list('too_dark.txt', input_dir, output_dir,
    #                                'time_lapse_dark.avi')
    log.info('Create a film with only dark images')
    photophoto.create_film_from_list(
        too_dark_2, input_dir, output_dir, fps, 'time_lapse_dark.avi')

    log.info('Create a film without dark images')
    photophoto.create_film_from_list(
        ok_images, input_dir, output_dir, fps, 'time_lapse_light.avi')

    log.info('Create a film with all images')
    photophoto.create_film_from_files(output_dir, fps, 'time_lapse_all.avi')

    end_time_nice = time.strftime('%H:%M:%S', time.localtime(end_time))
    time_now_nice = time.strftime('%H:%M:%S', time.localtime(time.time()))

    log.info('+-------------------------------------+')
    log.info('| Start time    | %s |          |' % (start_time_nice))
    log.info(
        '| Photos end    | %s | %s |' % (
            end_time_nice,
            str(datetime.timedelta(
                seconds=(int(end_time) - int(start_time))))))
    log.info(
        '| Requested end | %s | %s |' % (
            time_to_finish_nice,
            str(datetime.timedelta(
                seconds=(int(time_to_finish) - int(end_time))))))
    log.info(
        '| Total time    | %s | %s |' % (
            time_now_nice,
            str(datetime.timedelta(
                seconds=(int(time.time()) - int(start_time))))))
    log.info('+-------------------------------------+')
    log.info('And we are DONE!')


if __name__ == "__main__":
    main()
