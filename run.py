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

import argparse
import cv2
import signal

import util.environ_check
from util.camera import camera_factory
from util.window import Window
from util.sense_hat import Hat

from backend import backend_factory


class Cleanup(object):
    def __init__(self):
        self._stop_now = False
        signal.signal(signal.SIGINT, self._handler)
        signal.signal(signal.SIGTERM, self._handler)

    @property
    def stop_now(self):
        return self._stop_now

    def _handler(self, signum, frame):
        self._stop_now = True
        print('Signal %d' % signum)


def main(camera_id, backend_id, show_fps, detect_type, use_led):
    backend = backend_factory(backend_id)
    camera = camera_factory(camera_id)
    camera.open()
    window = Window(show_fps)
    window.open()
    hat = None
    if use_led:
        hat = Hat()
        hat.open()

    cleanup = Cleanup()

    while not cleanup.stop_now:
        ret, frame = camera.read()
        if not ret:
            break

        detected = (detect_type and backend.detect(detect_type))
        window.show_frame(backend.process_frame(frame),
                          detect_type if detected else None)
        if hat:
            hat.update_led(detected)

        key = cv2.waitKey(5) & 0xFF
        if key == ord('q') or key == 27:  # Pressing 'q' or ESC.
            break

    if hat:
        hat.close()
    window.close()
    camera.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Show camera preview")
    # -1 selects default camera.
    parser.add_argument('-c', '--camera', dest='camera_id', default='-1',
                        help='Set camera id.')
    parser.add_argument('-b', '--backend', dest='backend_id', default='0',
                        help='Set backend id.')
    parser.add_argument('-f', '--fps', dest='show_fps', default=False,
                        action='store_true', help='Show FPS info.')
    parser.add_argument('-d', '--detect', dest='detect_type', default=None,
                        help='Set object type to detect.')
    parser.add_argument('-l', '--led', dest='use_led', default=False,
                        action='store_true', help='Use Raspberry Pi Sense HAT Led.')
    args = parser.parse_args()
    main(args.camera_id, args.backend_id, args.show_fps, args.detect_type, args.use_led)
