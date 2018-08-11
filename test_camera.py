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

import util.environ_check
from util.camera import camera_factory
from util.window import Window


def main(camera_id):
    camera = camera_factory(camera_id)
    camera.open()

    window = Window()
    window.open()

    while True:
        ret, frame = camera.read()
        if not ret:
            break
        window.show_frame(frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    window.close()
    camera.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Show camera preview")
    # -1 selects default camera.
    parser.add_argument('-c', '--camera', dest='camera_id', default='-1',
                        help='camera id')
    args = parser.parse_args()
    main(args.camera_id)
