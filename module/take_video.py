import picamera

class TakeVideo(object):
    def __init__(self, time ,*args):
        super(TakeVideo, self).__init__(*args)
        self.camera = picamera.PiCamera()
        self.time = time

    def start_recording_with_time(self, file, time):
        name = file + ".h264"
        self.camera.start_recording(name)
        self.camera.wait_recording(time)
        self.camera.stop_recording()

    def start_recording(self, file):
        return self.start_recording_with_time(file, self.time)


