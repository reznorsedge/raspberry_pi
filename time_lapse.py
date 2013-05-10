#!/usr/bin/python
import time
import os
import subprocess
import logging


class Camera:
    def __init__(self):
        self.log = logging.getLogger('time_lapse.Camera')

    def take_photo(self, iteration, output_dir):
        self.log.debug('Take a picture. Iteration "%s"' % (iteration))
        output_file = output_dir + "/" + str(iteration).zfill(4) + ".jpg"
        subprocess.call(["fswebcam", "--save", output_file, "-r", "1280x720",
                "-q", "-d", "v4l2:/dev/video0", "-S", "15"])
        iteration += 1

    def create_film_from_files(self, output_dir):
        output_file = output_dir + "/time_lapse.avi"
        self.log.info('Create a video')
        self.log.debug("Running command with output dir: %s output file: %s"
                % (output_dir, output_file))
        subprocess.call(["mencoder", "mf://%s/*.jpg" % (output_dir), "-mf",
                "fps=24:type=jpg", "-ovc", "lavc", "-lavcopts",
                "vcodec=mpeg4:mbd=2:trell", "-oac", "copy", "-o", output_file])

    def create_film_from_list(self, input_file, output_dir,
            output_name="time_lapse.avi"):
        output_file = os.path.join(output_dir, output_name)
        self.log.info(
                'Create a video from list of filenames (%s)' % (input_file))
        self.log.debug('Running command with output dir "%s" and output file'
                        '%s' % (output_dir, output_name))
                        

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

    timenow = time.time()
    timetofinish = timenow + (time_to_run_mins * 60)
    iteration = 0

    photophoto = Camera()

    while timenow < timetofinish:
        photophoto.take_photo(iteration, output_dir)
        timenow = time.time()
        iteration += 1
        time.sleep(delay_between_shots)

    photophoto.create_film(output_dir)

    log.info('And we are DONE!')


if __name__ == "__main__":
    main()
