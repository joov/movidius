import cv2


def camera_factory(camera_id):
    if camera_id == 'pi':
        assert False, 'Pi camera is unsupported'
    else:
        return USBCamera(int(camera_id))


class USBCamera(object):
    def __init__(self, camera_id):
        self.device_index = camera_id
        self.capture = None

    def open(self):
        print('Opening USB camera %d' % self.device_index)
        self.capture = cv2.VideoCapture(self.device_index)

    def read(self):
        """Reads a frame.

        Returns (ret, frame)
        """
        assert self.capture is not None, 'Camera is not open'
        ret, frame = self.capture.read()
        if not ret:
            print('Failed to read camera %d' % self.device_index)
        return (ret, frame)

    def close(self):
        if self.capture:
            self.capture.release()
            self.capture = None
