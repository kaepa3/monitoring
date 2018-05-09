import picamera

class TakeVideo(object):
    def __init__(self, time ,*args):
        super(TakeVideo, self).__init__(*args)
        self.camera = picamera.PiCamera()
        self.time = time

    def start_recording_with_time(self, file, time):
        self.camera.start_recording(file)
        self.camera.wait_recording(time)
        self.camera.stop_recording()

    def start_recording(self, time):
        self.start_recording_with_time(file, self.time)


