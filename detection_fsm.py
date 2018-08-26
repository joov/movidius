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

import time

from util.speech import Speech


BOUNCE_TIME = 2000  # millisecs


def _current_millis():
    return int(round(time.time() * 1000))


class DetectionFSM(object):
    def __init__(self, play_speech):
        self._last_detection_time = None
        self._speech = None
        if play_speech:
            self._speech = Speech()

    def update_status(self, detected):
        """It only reports False after not detected for BOUNCE_TIME."""
        now = _current_millis()
        if detected:
            self._last_detection_time = now
            return True
        if (self._last_detection_time is not None and
                now - self._last_detection_time < BOUNCE_TIME):
            return True
        return False
