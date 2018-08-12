# Copyright (c) 2018 Chen-Ting Chuang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import cv2

try:
    from picamera.array import PiRGBArray
    from picamera import PiCamera
except ImportError:
    print('picamera[array] is not installed')
    print("Run 'pip3 install picamera[array]' " +
          "if you're using Raspberry Pi camera\n")


_CAMERA_WIDTH = 640
_CAMERA_HEIGHT = 480

# Hack: drop queued v4l2 frames until the last one.
# IIRC the magic number is decided somewhere in V4L2 or UVC layer in kernel.
# Assume kernel queues 5 frames, then drop the first 4 frames.
# TODO: we should be able to VIDIOC_DQBUF V4L2 buffer, but I'm not
#       sure if OpenCV supports this operation.
_DROP_FRAME_QUEUE = 4


def camera_factory(camera_id):
    if camera_id == 'pi':
        return _RaspberryCamera()
    else:
        return _USBCamera(int(camera_id))


# def _crop_frame(frame):
#     x_offset = int((_CAMERA_WIDTH - _CAMERA_CROPPED_WIDTH) / 2)
#     return frame[:, x_offset:x_offset + _CAMERA_CROPPED_WIDTH]


class _USBCamera(object):
    def __init__(self, camera_id):
        self.device_index = camera_id
        self.capture = None

    def open(self):
        print('Opening USB camera %d' % self.device_index)
        self.capture = cv2.VideoCapture(self.device_index)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, _CAMERA_WIDTH)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, _CAMERA_HEIGHT)

    def read(self):
        """Reads a frame.

        Returns (ret, frame)
        """
        assert self.capture is not None, 'Camera is not open'
        if _DROP_FRAME_QUEUE > 0:
            for i in range(_DROP_FRAME_QUEUE):
                self.capture.grab()
        ret, frame = self.capture.read()
        if not ret:
            print('Failed to read camera %d' % self.device_index)
        return (ret, frame)

    def close(self):
        if self.capture:
            self.capture.release()
            self.capture = None


class _RaspberryCamera(object):
    def __init__(self):
        self.camera = None

    def open(self):
        self.camera = PiCamera()
        self.camera.resolution = (_CAMERA_WIDTH, _CAMERA_HEIGHT)

    def read(self):
        """Reads a frame.

        Returns (ret, frame)
        """
        try:
            # TODO: PiRGBArray is extremely slow (<2FPS). No good solution yet.
            with PiRGBArray(self.camera) as capture:
                self.camera.capture(capture, format='bgr')
                return True, capture.array
        except Exception as e:
            print('Failed to read from Raspberry Pi camera %r' % e)
            return False, None

    def close(self):
        pass
