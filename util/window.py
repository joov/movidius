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
import time


_WINDOW = 'preview'

# Resize to fit my 480x320 display on RPi3 with the same aspect ratio 
# of 640x480.
_RESIZE_WIDTH = 427
_RESIZE_HEIGHT = 320


def _current_millis():
    return int(round(time.time() * 1000))


class Window(object):
    def __init__(self, show_fps=False):
        self.show_fps = show_fps
        self.last_time = _current_millis()
        self.frame_count = 0
        self.fps_text = ''

    def open(self):
        cv2.namedWindow(_WINDOW, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(_WINDOW, cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN)

    @staticmethod
    def _fps_text(frame, text):
        if not text:
            return
        height = frame.shape[0]
        cv2.putText(frame, text, (20, height - 30),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 5)
        cv2.putText(frame, text, (20, height - 30),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 100, 0), 2)

    def show_frame(self, frame):
        frame = cv2.resize(frame, (_RESIZE_WIDTH, _RESIZE_HEIGHT))
        if self.show_fps:
            now = _current_millis()
            self.frame_count += 1
            if (now - self.last_time) > 1500:
                fps = self.frame_count * 1000.0 / float(now - self.last_time)
                self.last_time = now
                self.frame_count = 0
                self.fps_text = 'fps: %.2f' % fps
                print(self.fps_text)
            self._fps_text(frame, self.fps_text)
        cv2.imshow(_WINDOW, frame)

    def close(self):
        cv2.destroyAllWindows()
