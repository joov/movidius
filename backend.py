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


def backend_factory(backend_id):
    backend_index = int(backend_id)
    if backend_index == 0:
        print('Use Keras/Tensorflow backend.')
        return _KerasBackend()
    elif backend_index == 1:
        print('Use Movidius NCS backend.')
        return _YoloV2NCS_Backend()


class _KerasBackend(object):
    def __init__(self):
        from vendor.keras_yolo3.yolo import YOLO
        self.yolo = YOLO()

    def __del__(self):
        self.yolo.close_session()

    def process_frame(self, frame):
        import numpy as np
        from PIL import Image
        image = Image.fromarray(frame)
        image = self.yolo.detect_image(image)
        return np.asarray(image)


class _YoloV2NCS_Backend(object):
    def __init__(self):
        from vendor.YoloV2NCS.detectionExample.ObjectWrapper import ObjectWrapper
        self.wrapper = ObjectWrapper('vendor/YoloV2NCS/graph')

    def process_frame(self, frame):
        from vendor.YoloV2NCS.detectionExample.Visualize import Visualize
        return Visualize(frame, self.wrapper.Detect(frame))
